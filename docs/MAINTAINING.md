# 维护指南

本仓库是 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) 的**中文镜像**，所有 `README.md` / `categories/*.md` 都由 `scripts/sync_translate.py` 自动翻译生成，**请勿直接手工编辑**。

## 工作原理

```
┌──────────────────────┐  git clone/pull  ┌─────────────────────────┐
│ VoltAgent 上游仓库    │ ───────────────▶ │ cache/upstream/          │
└──────────────────────┘                  └──────────┬──────────────┘
                                                      │ sha256 diff
                                                      ▼
                              ┌─────────────────────────────────────┐
                              │ 对比 cache/state.json 里的历史 hash  │
                              │  找出新增 / 已修改 / 已删除的文件     │
                              └──────────┬──────────────────────────┘
                                         │ 仅变更文件
                                         ▼
                   ┌───────────────────────────────────────────┐
                   │ Amazon Bedrock Converse API (Claude 4.6)  │
                   │  按 40KB/chunk 切分，chunk 级缓存命中则跳过 │
                   └──────────┬────────────────────────────────┘
                              ▼
                    categories/*.md + README.md
```

**增量策略**：
1. **文件级 hash**：每个上游 markdown 文件的 sha256 记录在 `cache/state.json`。只有 hash 变了的文件才会翻译。
2. **chunk 级缓存**：单个文件内部也按 chunk 缓存在 `cache/chunks/<sha256>.md`；同一段英文内容再出现（比如大文件中途失败重跑、或不同文件出现相同段落）直接命中缓存，不再调 Bedrock。
3. **失败安全**：进程被 `kill -9` 后，**已成功翻译的文件 hash 才会写入 state**，未完成的文件下次自动重跑；chunk 缓存让重跑时已完成的 chunk 不会重复调用 API。

## 日常使用

### 首次初始化

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# AWS 凭证：按常规方式配置即可（aws configure / SSO / 环境变量）
aws sts get-caller-identity      # 验证能访问 Bedrock
```

### 增量更新（日常使用）

```bash
python scripts/sync_translate.py
```

脚本会：
1. `git pull` 上游到 `cache/upstream/`
2. 对比 hash，只翻译变更 / 新增的文件
3. 更新 `categories/*.md`、`README.md` 和 `cache/state.json`

多数情况下上游一天只有几个文件有变更，增量翻译几十秒到几分钟就完成。

### 常用参数

| 命令 | 用途 |
|------|------|
| `python scripts/sync_translate.py --dry-run` | 只看哪些文件会被翻译，不真的调用 Bedrock |
| `python scripts/sync_translate.py --force` | 强制重翻所有文件（用于改了 prompt 想整体刷新） |
| `python scripts/sync_translate.py --only gaming.md` | 只翻某一个文件（子串匹配） |
| `python scripts/sync_translate.py --skip-sync` | 不拉 upstream，直接用本地 `cache/upstream/` 的内容 |
| `python scripts/sync_translate.py --no-translate` | 同步 + 检测差异，但不调 Bedrock（通常配合 `-v`） |
| `python scripts/sync_translate.py --concurrency 3` | 每个文件内 chunk 并发数（默认 1；网络好可调到 3） |
| `python scripts/sync_translate.py -v` | 调试日志 |

### 后台长跑（大文件）

macOS 上因 shell 超时容易杀死翻译进程，用 `scripts/detach.py` 彻底脱离父进程：

```bash
python scripts/detach.py           # 跑常规增量
python scripts/detach.py --force   # 或任意其它参数

# 查看进度
tail -f cache/logs/sync.log
# 查看 PID
ps -ef | grep sync_translate | grep -v grep
```

## 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `BEDROCK_MODEL_ID` | `global.anthropic.claude-sonnet-4-6` | 推荐 Sonnet 4.6（1M 上下文、输出 64K）。如 Bedrock 区域拥堵，临时换 `global.anthropic.claude-haiku-4-5-20251001-v1:0` 可加速 ~5 倍，质量略降 |
| `BEDROCK_REGION` | `us-west-2` | 可改 `us-east-1` 等，注意必须是对应 inference profile 可用的区域 |
| `BEDROCK_MAX_TOKENS` | `64000` | 单次响应最大输出 token |
| `AWS_REGION` / 其他 boto3 凭证 | - | 按 boto3 标准规则读取 |

## 翻译质量控制

### 改翻译规则

翻译行为由 `scripts/sync_translate.py` 中的 `SYSTEM_PROMPT` 常量控制：

- 要统一术语（如把"代理"改回"代理人"、或"技能"改成"能力"），改 `SYSTEM_PROMPT` 第 5 条
- 要改变风格（更正式 / 更口语），改开头的 tone 描述
- 改完后用 `--force` 重翻一次；如只测小范围：`--force --only gaming.md`

### 验证条目完整性

翻译后可以跑下面的检查脚本，比对上游与本地各文件的 list item 数量：

```bash
python3 <<'PY'
from pathlib import Path
import re
def count(path):
    return len(re.findall(r'^- \[', path.read_text(), re.MULTILINE))
for f in sorted(Path('cache/upstream/categories').glob('*.md')):
    up = count(f)
    local_path = Path('categories') / f.name
    if not local_path.exists():
        print(f'  MISSING {f.name}')
        continue
    local = count(local_path)
    if up != local:
        print(f'  DIFF {f.name}  upstream={up}  local={local}')
PY
```

上游与本地条目数一致即说明翻译完整、无截断。

### 失败重试

Bedrock 偶尔会因网络 / 服务端负载 `ConnectionClosedError`。脚本内置 5 次指数退避重试；如全部失败：
1. 该文件的 hash 不会写入 state，下次 `sync_translate.py` 自动重做
2. 已成功的 chunk 留在 `cache/chunks/`，不会浪费

强制清 chunk 缓存（一般不需要）：

```bash
rm -rf cache/chunks/
```

## 目录结构

```
awesome-skills-deepdive/
├── README.md                       ← 上游 README 中文翻译（自动生成）
├── categories/                     ← 上游 categories 中文翻译（自动生成）
│   ├── ai-and-llms.md
│   ├── coding-agents-and-ides.md
│   └── ... (30 个分类)
├── scripts/
│   ├── sync_translate.py           ← 主脚本
│   └── detach.py                   ← 后台启动辅助
├── cache/
│   ├── upstream/                   ← git clone 的上游仓库（.gitignore）
│   ├── chunks/                     ← 翻译 chunk 缓存（.gitignore）
│   ├── logs/                       ← 运行日志（.gitignore）
│   └── state.json                  ← 文件级 hash 状态（提交，用于增量）
├── requirements.txt
└── docs/MAINTAINING.md             ← 本文档
```

## 已知限制

1. **输出 token 上限 64K**。超过 80KB 英文的文件会被拆成多个 chunk（如果 chunk 再被截断，脚本会报 `Output truncated by max_tokens`，调 `BEDROCK_MAX_TOKENS` 或减小 chunk 阈值 `SINGLE_SHOT_MAX_CHARS`）。
2. **区域拥堵**。实测 us-west-2 在美西工作时间段 Sonnet 4.6 响应偶尔会变慢或卡死。不急的话换时段再跑；急的话切 Haiku 或换 region。
3. **没做语义校验**。脚本只保证 Markdown 结构 + 条目数量对齐，不检查翻译内容是否准确。偶尔模型会漏翻或改动 slug，肉眼抽查一下最好。
