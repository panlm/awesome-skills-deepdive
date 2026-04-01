# my-tesla

> 通过 Tesla API 控制和监控 Tesla 车辆

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | my-tesla |
| **作者** | officialpm |
| **ClawHub** | https://clawskills.sh/skills/officialpm-my-tesla |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/officialpm/my-tesla |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Python 3.10+
- Token cache: `~/.tesla_cache.json` (local only; best-effort chmod `0600`)
- Optional: set `MY_TESLA_DEFAULT_CAR` to a vehicle display name to pick a default car via env var
- Or persist a local default with: `python3 {baseDir}/scripts/tesla.py default-car "Name"` (writes `~/.my_tesla.json`; best-effort chmod `0600`)

## 使用场景

Connects to the Tesla Owner API via teslapy to control and monitor Tesla vehicles from macOS. Supports checking vehicle state, running remote commands, and tracking mileage locally. Auth tokens are cached on disk; disruptive actions require explicit confirmation.

## 依赖和前提条件

- macOS 系统
- Python 3
- teslapy (Python)

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
TESLA_EMAIL="you@email.com" python3 {baseDir}/scripts/tesla.py auth
, bash
# List vehicles
python3 {baseDir}/scripts/tesla.py list
python3 {baseDir}/scripts/tesla.py list --json   # machine-readable, privacy-safe

# Version
python3 {baseDir}/scripts/tesla.py version
python3 {baseDir}/scripts/tesla.py --version

# Debugging
# If something fails unexpectedly, add --debug for a full traceback
# (or set MY_TESLA_DEBUG=1)
python3 {baseDir}/scripts/tesla.py --debug status --no-wake

# Pick a car (optional)
# --car accepts: exact name, partial name (substring match), or a 1-based index from  |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。执行 shell 命令: bash
TESLA_EMAIL="you@email.com" pyth

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
