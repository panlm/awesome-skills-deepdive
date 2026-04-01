# n2-stitch-mcp

> Resilient MCP proxy for Google Stitch — 3-layer safety (auto-retry, token refresh, TCP drop recovery).

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | n2-stitch-mcp |
| **作者** | choihyunsus |
| **ClawHub** | https://clawskills.sh/skills/choihyunsus-n2-stitch-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/choihyunsus/n2-stitch-mcp |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **create_project** — Create a Stitch project
- **list_projects** — List all projects
- **get_project** — Get project details
- **list_screens** — List screens in a project
- **get_screen** — Get screen HTML/CSS
- **generate_screen_from_text** — ✨ Generate UI from text (Resilient!)

## 依赖和前提条件

- STITCH_API_KEY

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
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key, api key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟡 警告 | 注意: list all |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 3 项警告: 命令执行, 凭证获取, 越权操作。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
