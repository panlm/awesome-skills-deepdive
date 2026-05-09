#!/usr/bin/env python3
"""
sync_translate.py

Sync the upstream VoltAgent/awesome-openclaw-skills repository and produce a
Chinese-translated mirror, with incremental updates driven by file-level hashes.

Design:
  - Clone / pull upstream into cache/upstream
  - For every markdown file under categories/ (and README.md), compare sha256
    with previous state stored in cache/state.json
  - Only re-translate changed / new files
  - Use Amazon Bedrock (Claude family) for translation with chunked requests
  - Preserve Markdown structure: links, slugs, code blocks, tables, badges

Usage:
  python scripts/sync_translate.py                      # incremental
  python scripts/sync_translate.py --dry-run            # show plan only
  python scripts/sync_translate.py --force              # retranslate everything
  python scripts/sync_translate.py --only git-and-github  # limit to one file
  python scripts/sync_translate.py --skip-sync          # do not touch upstream clone
  python scripts/sync_translate.py --no-translate       # sync + detect only

Environment variables:
  BEDROCK_MODEL_ID          primary model, default global.anthropic.claude-sonnet-4-6 (1M context)
  BEDROCK_FALLBACK_MODEL_ID fallback on timeout / truncation, default global.anthropic.claude-haiku-4-5-20251001-v1:0
  BEDROCK_REGION            default: us-west-2 (or $AWS_REGION)
  BEDROCK_MAX_TOKENS        default: 64000 (Sonnet 4.6 output ceiling)
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import logging
import os
import subprocess
import sys
import textwrap
import time
from pathlib import Path
from typing import Iterable

# --------------------------------------------------------------------------- #
# Paths & constants
# --------------------------------------------------------------------------- #

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM_URL = "https://github.com/VoltAgent/awesome-openclaw-skills.git"
UPSTREAM_DIR = ROOT / "cache" / "upstream"
STATE_FILE = ROOT / "cache" / "state.json"
CHUNK_CACHE_DIR = ROOT / "cache" / "chunks"
LOG_DIR = ROOT / "cache" / "logs"
OUTPUT_CATEGORIES = ROOT / "categories"
OUTPUT_README = ROOT / "README.md"

# Files considered for translation (relative to upstream root)
TRANSLATION_TARGETS = {
    "README.md": OUTPUT_README,
    # categories/*.md are discovered dynamically
}

# --------------------------------------------------------------------------- #
# Logging
# --------------------------------------------------------------------------- #

def setup_logging(verbose: bool = False) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_DIR / "sync.log", encoding="utf-8"),
        ],
    )

log = logging.getLogger("sync")

# --------------------------------------------------------------------------- #
# State management
# --------------------------------------------------------------------------- #

@dataclasses.dataclass
class State:
    upstream_commit: str = ""
    file_hashes: dict[str, str] = dataclasses.field(default_factory=dict)
    last_run: str = ""

    @classmethod
    def load(cls) -> "State":
        if not STATE_FILE.exists():
            return cls()
        try:
            data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
            return cls(
                upstream_commit=data.get("upstream_commit", ""),
                file_hashes=data.get("file_hashes", {}),
                last_run=data.get("last_run", ""),
            )
        except Exception as exc:  # noqa: BLE001
            log.warning("state.json unreadable (%s), starting fresh", exc)
            return cls()

    def save(self) -> None:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(
            json.dumps(dataclasses.asdict(self), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

# --------------------------------------------------------------------------- #
# Git sync
# --------------------------------------------------------------------------- #

def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    log.debug("$ %s (cwd=%s)", " ".join(cmd), cwd)
    result = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        check=check,
        text=True,
        capture_output=True,
    )
    if result.stdout:
        log.debug(result.stdout.strip())
    if result.returncode != 0 and check:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{result.stderr}")
    return result.stdout.strip()


def sync_upstream() -> str:
    """Clone or pull upstream. Returns current HEAD commit sha."""
    if not UPSTREAM_DIR.exists() or not (UPSTREAM_DIR / ".git").exists():
        UPSTREAM_DIR.parent.mkdir(parents=True, exist_ok=True)
        log.info("cloning upstream -> %s", UPSTREAM_DIR)
        run(["git", "clone", "--depth=1", UPSTREAM_URL, str(UPSTREAM_DIR)])
    else:
        log.info("pulling upstream updates")
        run(["git", "fetch", "--depth=1", "origin", "main"], cwd=UPSTREAM_DIR)
        run(["git", "reset", "--hard", "origin/main"], cwd=UPSTREAM_DIR)
    sha = run(["git", "rev-parse", "HEAD"], cwd=UPSTREAM_DIR)
    log.info("upstream HEAD: %s", sha[:12])
    return sha

# --------------------------------------------------------------------------- #
# Change detection
# --------------------------------------------------------------------------- #

def collect_upstream_files() -> list[Path]:
    """Return list of markdown files we care about, relative paths under upstream."""
    files: list[Path] = []
    readme = UPSTREAM_DIR / "README.md"
    if readme.exists():
        files.append(readme)
    categories = UPSTREAM_DIR / "categories"
    if categories.exists():
        files.extend(sorted(categories.glob("*.md")))
    return files


def detect_changes(
    state: State, force: bool, only: str | None
) -> tuple[list[tuple[Path, str]], list[Path], list[str]]:
    """Return (files_to_translate_with_new_hash, unchanged, removed_keys).

    IMPORTANT: does NOT mutate state.file_hashes. The caller is responsible
    for persisting hashes only after a file is successfully translated, so
    that a kill -9 midway never marks un-translated files as 'done'.
    """
    upstream_files = collect_upstream_files()
    upstream_rel = {str(p.relative_to(UPSTREAM_DIR)): p for p in upstream_files}

    to_translate: list[tuple[Path, str]] = []  # (path, new_hash)
    unchanged: list[Path] = []

    for rel, path in upstream_rel.items():
        if only and only not in rel:
            continue

        h = sha256_of(path)
        prev = state.file_hashes.get(rel)
        if force or prev != h:
            to_translate.append((path, h))
        else:
            unchanged.append(path)

    removed = sorted(set(state.file_hashes) - set(upstream_rel))
    return to_translate, unchanged, removed

# --------------------------------------------------------------------------- #
# Bedrock Client
# --------------------------------------------------------------------------- #

class BedrockClient:
    DEFAULT_MODEL = os.environ.get(
        "BEDROCK_MODEL_ID",
        "global.anthropic.claude-sonnet-4-6",
    )
    DEFAULT_FAST_MODEL = os.environ.get(
        "BEDROCK_FAST_MODEL_ID",
        "global.anthropic.claude-haiku-4-5-20251001-v1:0",
    )
    DEFAULT_REGION = os.environ.get("BEDROCK_REGION") or os.environ.get(
        "AWS_REGION", "us-west-2"
    )
    MAX_TOKENS = int(os.environ.get("BEDROCK_MAX_TOKENS", "64000"))
    MAX_RETRIES = 5
    BACKOFF_BASE = 2.0

    def __init__(
        self,
        model_id: str | None = None,
        region: str | None = None,
        fast_model_id: str | None = None,
    ):
        import boto3
        from botocore.config import Config as BotoConfig

        self.model_id = model_id or self.DEFAULT_MODEL
        self.fast_model_id = fast_model_id or self.DEFAULT_FAST_MODEL
        self.region = region or self.DEFAULT_REGION
        self.client = boto3.client(
            "bedrock-runtime",
            region_name=self.region,
            config=BotoConfig(
                read_timeout=600,
                connect_timeout=30,
                retries={"max_attempts": 1},
            ),
        )
        log.info(
            "Bedrock client ready: primary=%s fast=%s region=%s",
            self.model_id,
            self.fast_model_id,
            self.region,
        )

    def translate(self, system: str, user: str, model_id: str | None = None) -> str:
        """Call Bedrock Converse API with retry + backoff."""
        mid = model_id or self.model_id
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                resp = self.client.converse(
                    modelId=mid,
                    system=[{"text": system}],
                    messages=[
                        {"role": "user", "content": [{"text": user}]},
                    ],
                    inferenceConfig={
                        "maxTokens": self.MAX_TOKENS,
                        "temperature": 0,
                    },
                )
                stop = resp.get("stopReason", "")
                if stop == "max_tokens":
                    raise RuntimeError(
                        f"Output truncated by max_tokens (model={mid}, current={self.MAX_TOKENS})"
                    )
                message = resp.get("output", {}).get("message", {})
                parts = message.get("content", []) or []
                text = "".join(p.get("text", "") for p in parts if "text" in p)
                if not text:
                    raise RuntimeError(f"empty response from Bedrock (stop={stop})")
                return text.strip()
            except Exception as exc:  # noqa: BLE001
                name = type(exc).__name__
                if name in ("ValidationException", "AccessDeniedException"):
                    raise
                wait = self.BACKOFF_BASE ** attempt
                log.warning(
                    "bedrock converse failed on %s (attempt %d/%d, %s): %s -- sleeping %.1fs",
                    mid,
                    attempt,
                    self.MAX_RETRIES,
                    name,
                    exc,
                    wait,
                )
                if attempt == self.MAX_RETRIES:
                    raise
                time.sleep(wait)
        raise RuntimeError("unreachable")

# --------------------------------------------------------------------------- #
# Translator
# --------------------------------------------------------------------------- #
#
# Design: no chunking. Send the whole file to Bedrock in one request. Sonnet
# 4.6 supports 1M input tokens, so inputs are never a problem; the only risk
# is output exceeding max_tokens / connection timeout on very large files.
# If that happens the caller sees a clear error and can decide what to do
# (run again, switch model, etc.). The file-level hash + chunk cache below
# ensure failed files are retried next run without wasting Bedrock credits
# on already-translated content.

SYSTEM_PROMPT = textwrap.dedent(
    """\
    You are a professional technical translator. You receive Markdown fragments
    from an open-source "awesome list" catalog of AI agent skills, and return
    the same fragment translated into Simplified Chinese (简体中文).

    Strict rules (follow ALL):
    1. Output **only** the translated Markdown. Do not add explanations,
       preambles, or code fences around the whole answer.
    2. Preserve the Markdown structure **exactly**: headings levels, list
       markers, blockquotes, table pipes, indentation, and blank lines.
    3. DO translate (this is what the reader is here for):
       - ALL headings `#`, `##`, `###` — even if the heading is a short English
         word like "Gaming" → "游戏", "Installation" → "安装".
       - Navigation / UI phrases like `← Back to main list` → `← 返回主列表`.
       - Counts and labels like `**36 skills**` → `**36 个技能**`,
         `View all 159 skills in ...` → `查看 ... 分类下的全部 159 个技能`.
       - Prose paragraphs, blockquotes, table cells.
       - The description portion AFTER the link in a list item, e.g.
         `- [slug](url) - DESCRIPTION` — translate DESCRIPTION only.
       - Skill category names when they appear in running text.
    4. DO NOT translate, change, or re-wrap:
       - URLs, link targets, image paths, HTML anchors `#foo-bar`.
       - HTML tags and attributes.
       - Content inside fenced code blocks (``` ... ```) or inline code (`...`).
       - Shell / config / JSON / YAML snippets and command names.
       - Slug-style link TEXT that looks like an identifier (contains hyphens,
         no spaces, all lowercase), e.g. `[agent-commons]`, `[skill-slug]`,
         `[clawhub-cli]` — keep the slug as-is inside the brackets.
       - Badge image URLs, shields.io parameters, base64 blobs.
       - Proper nouns / product names without a widely-used Chinese form
         (e.g. "OpenClaw", "ClawHub", "GitHub", "Bedrock", "Claude", "MCP").
    5. Keep technical terms accurate. Prefer these canonical translations:
       - agent → 智能体   (preferred over 代理)
       - skill → 技能
       - workflow → 工作流
       - registry / hub → 注册表 / 平台
       - plugin → 插件
       - prompt → 提示词
       - fine-tune → 微调
       - endpoint → 端点
       - repository / repo → 仓库
       - orchestration → 编排
       Common acronyms stay in English (API, CLI, SDK, OAuth, LLM, RAG, MCP).
    6. HTML anchor lines produced by GitHub like `[](#git--github)` must
       remain BYTE-IDENTICAL. Never translate anchors.
    7. If the original already contains Chinese, keep it unchanged.
    8. Never invent information that isn't in the source. If something is
       ambiguous, translate literally rather than paraphrase.
    9. Keep a calm, encyclopedic tone. Do not add emojis that weren't there.
    """
)


# Files larger than this are routed to the fast model (Haiku) because Sonnet
# on Bedrock cannot stream back ~100K tokens within the 20-minute read timeout.
LARGE_FILE_THRESHOLD = int(os.environ.get("LARGE_FILE_THRESHOLD", "100000"))


def translate_chunk(client: BedrockClient, chunk: str, model_id: str | None = None) -> str:
    """Translate markdown. Cache key includes model_id so switching models
    doesn't accidentally reuse a lower-quality translation."""
    key_src = f"{model_id or client.model_id}\n{chunk}".encode("utf-8")
    key = hashlib.sha256(key_src).hexdigest()
    cache_path = CHUNK_CACHE_DIR / f"{key}.md"
    if cache_path.exists():
        log.debug("    translation cache hit: %s", key[:12])
        return cache_path.read_text(encoding="utf-8")

    user = (
        "Translate the following Markdown document into Simplified Chinese,"
        " obeying every rule in the system prompt.\n\n"
        "<<<MARKDOWN>>>\n"
        f"{chunk}\n"
        "<<<END>>>"
    )
    out = client.translate(SYSTEM_PROMPT, user, model_id=model_id)
    if out.startswith("```") and out.rstrip().endswith("```"):
        lines = out.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        out = "\n".join(lines)
    CHUNK_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(out, encoding="utf-8")
    return out


def translate_markdown(client: BedrockClient, source: str) -> str:
    """Translate an entire markdown file in a single Bedrock call.
    Files larger than LARGE_FILE_THRESHOLD are routed to the fast model
    (Haiku) so their ~100K output tokens arrive before the 20-minute timeout.
    """
    if len(source) > LARGE_FILE_THRESHOLD:
        model_id = client.fast_model_id
        log.info(
            "  file is %d chars (> %d) — using FAST model %s",
            len(source),
            LARGE_FILE_THRESHOLD,
            model_id,
        )
    else:
        model_id = None  # primary (Sonnet)
        log.info("  sending whole file to Bedrock (%d chars)", len(source))
    translated = translate_chunk(client, source, model_id=model_id)
    return translated.rstrip() + "\n"

# --------------------------------------------------------------------------- #
# Orchestrator
# --------------------------------------------------------------------------- #

def output_path_for(rel: str) -> Path:
    if rel == "README.md":
        return OUTPUT_README
    if rel.startswith("categories/"):
        return ROOT / rel
    return ROOT / rel


def translate_file(client: BedrockClient, upstream_path: Path) -> Path:
    rel = str(upstream_path.relative_to(UPSTREAM_DIR))
    out_path = output_path_for(rel)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    source = upstream_path.read_text(encoding="utf-8")
    log.info("translating %s (%d chars) -> %s", rel, len(source), out_path.relative_to(ROOT))
    translated = translate_markdown(client, source)

    # maintenance comment (invisible on GitHub UI but useful when opening the file)
    header = textwrap.dedent(
        f"""\
        <!--
          This file is auto-translated from upstream:
          {UPSTREAM_URL}
          source: {rel}
          Do NOT edit manually — run scripts/sync_translate.py to update.
        -->

        """
    )

    # For README.md, add a visible banner pointing to the English original
    if rel == "README.md":
        banner = textwrap.dedent(
            f"""\
            > **中文镜像版** · 本仓库是 [VoltAgent/awesome-openclaw-skills]({UPSTREAM_URL.replace('.git', '')}) 的自动翻译镜像。
            > 查看英文原版请前往上游仓库；本地维护请见 [`docs/MAINTAINING.md`](./docs/MAINTAINING.md)。

            ---

            """
        )
        translated = banner + translated

    out_path.write_text(header + translated, encoding="utf-8")
    return out_path


def remove_stale(removed_keys: Iterable[str]) -> None:
    for rel in removed_keys:
        target = output_path_for(rel)
        if target.exists():
            log.info("removing stale translation %s", target.relative_to(ROOT))
            target.unlink()

# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true", help="show plan without calling Bedrock")
    p.add_argument("--force", action="store_true", help="re-translate all tracked files")
    p.add_argument("--only", help="substring match: only translate files whose path contains this")
    p.add_argument("--skip-sync", action="store_true", help="do not touch upstream clone")
    p.add_argument("--no-translate", action="store_true", help="sync + detect only, do not call Bedrock")
    p.add_argument("-v", "--verbose", action="store_true", help="debug logging")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(args.verbose)

    state = State.load()

    if args.skip_sync:
        if not UPSTREAM_DIR.exists():
            log.error("--skip-sync but upstream clone missing: %s", UPSTREAM_DIR)
            return 2
        upstream_sha = run(["git", "rev-parse", "HEAD"], cwd=UPSTREAM_DIR)
    else:
        upstream_sha = sync_upstream()

    to_translate, unchanged, removed = detect_changes(state, force=args.force, only=args.only)

    log.info(
        "plan: %d to translate, %d unchanged, %d removed upstream",
        len(to_translate),
        len(unchanged),
        len(removed),
    )
    for path, _ in to_translate:
        log.info("  translate: %s", path.relative_to(UPSTREAM_DIR))
    for rel in removed:
        log.info("  remove   : %s", rel)

    if args.dry_run:
        log.info("dry-run — no changes written")
        return 0

    remove_stale(removed)
    # also drop their hashes
    for rel in removed:
        state.file_hashes.pop(rel, None)
    if removed:
        state.save()

    if to_translate and not args.no_translate:
        client = BedrockClient()
        succeeded: list[Path] = []
        failed: list[tuple[Path, Exception]] = []
        for i, (path, new_hash) in enumerate(to_translate, start=1):
            rel = str(path.relative_to(UPSTREAM_DIR))
            log.info("[%d/%d] %s", i, len(to_translate), rel)
            try:
                translate_file(client, path)
                succeeded.append(path)
                # persist hash ONLY after successful write
                state.file_hashes[rel] = new_hash
                state.upstream_commit = upstream_sha
                state.last_run = time.strftime("%Y-%m-%dT%H:%M:%S%z")
                state.save()
            except Exception as exc:  # noqa: BLE001
                log.exception("failed to translate %s: %s", path, exc)
                # do NOT write hash -> next run will retry
                failed.append((path, exc))

        log.info("done: %d ok, %d failed", len(succeeded), len(failed))
        if failed:
            for p, e in failed:
                log.error("FAILED %s: %s", p.relative_to(UPSTREAM_DIR), e)
            return 1
    else:
        if args.no_translate:
            log.info("--no-translate flag, skipping Bedrock calls")
        else:
            log.info("nothing to translate")

    state.upstream_commit = upstream_sha
    state.last_run = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    state.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
