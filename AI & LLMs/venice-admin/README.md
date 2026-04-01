# venice-admin

> Venice AI account administration - check balance, view usage history, and manage API keys. Requires an Admin API key.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | venice-admin |
| **作者** | sabrinaaquino |
| **ClawHub** | https://clawskills.sh/skills/sabrinaaquino-venice-admin |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sabrinaaquino/venice-admin |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Whether you can consume (has balance)
- Current consumption currency (DIEM or USD)
- DIEM balance and epoch allocation
- USD balance
- `--currency`: Filter by currency: `DIEM`, `USD`, `VCU` (default: `DIEM`)
- `--start-date`: Start date filter (ISO format: `2024-01-01`)

## 依赖和前提条件

- Admin API key
- **Admin API key
- ["VENICE_API_KEY
- "VENICE_API_KEY
- VENICE_API_KEY="your_admin_api_key

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟡 警告 | 注意: https://api., httpx |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🔴 危险 | 检测到: admin |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 越权操作。 另有 5 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
