# vincent-credentials

> Secure credential management for agents. Use this skill when users need to store API keys, passwords, OAuth tokens, or SSH keys and write them to .env files without exposing values. Triggers on "store credentials", "API key", "manage secrets", "write to env", ".env file", "credential", "password", "

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | vincent-credentials |
| **作者** | glitch003 |
| **ClawHub** | https://clawskills.sh/skills/glitch003-vincent-credentials |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/glitch003/vincent-credentials |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- ${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/credentials/credentials
- ./credentials
- **Creation**: The agent runs `secret create` with `--type CREDENTIALS` — the CLI stores the API key automatically and returns a `keyId` and `claimUrl`.
- **Value set**: The user sets the credential value via the dashboard after claiming, or the agent sets it via the CLI.
- **Write to .env**: The agent runs `secret env` to write the value to a `.env` file without exposing it.
- **Claim**: The human operator uses the claim URL to take ownership and manage the secret from the dashboard.

## 依赖和前提条件

- ACME_API_KEY
- "ACME_API_KEY
- `MY_API_KEY
- `OAUTH_TOKEN
- SERVICE_TOKEN

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: password, api key |
| SEC-04 供应链风险 | 🟡 警告 | 注意: @latest |
| SEC-05 文件系统篡改 | 🟡 警告 | 注意: write them to .env file, write to env", ".env file |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 6 项警告: 命令执行, 凭证获取, 供应链风险, 文件系统篡改, Prompt 注入, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
