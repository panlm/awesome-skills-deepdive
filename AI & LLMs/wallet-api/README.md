# wallet-api

> Interact with the BudgetBakers Wallet API for personal finance data. Use when the user needs to query accounts, categories, transactions (records), budgets, or templates from their Wallet app via the REST API. Requires WALLET_API_TOKEN environment variable.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | wallet-api |
| **作者** | andresubri |
| **ClawHub** | https://clawskills.sh/skills/andresubri-wallet-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andresubri/wallet-api |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Authentication details
- Rate limiting (500 req/hour)
- Query filter syntax (text and range filters)
- Pagination parameters
- Data synchronization behavior
- Agent hints

## 依赖和前提条件

- WALLET_API_TOKEN
- `WALLET_API_TOKEN
- WALLET_API_TOKEN="your_token

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 2 项警告: 命令执行, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
