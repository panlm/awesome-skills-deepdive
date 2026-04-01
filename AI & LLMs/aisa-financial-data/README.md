# aisa-financial-data

> Query real-time and historical financial data across equities and crypto—prices, market moves, metrics, and trends for analysis, alerts, and reporting.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | aisa-financial-data |
| **作者** | aisapay |
| **ClawHub** | https://clawskills.sh/skills/aisapay-aisa-financial-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-financial-data |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- `ticker`: Stock symbol (required)
- `interval`: `second`, `minute`, `day`, `week`, `month`, `year` (required)
- `interval_multiplier`: Multiplier for interval, e.g., 5 for 5-minute bars (required)
- `start_date`: Start date YYYY-MM-DD (required)
- `end_date`: End date YYYY-MM-DD (required)

## 依赖和前提条件

- {"openclaw":{"emoji":"📊","requires":{"bins":["curl","python3"],"env":["AISA_API_KEY"]},"primaryEnv":"AISA_API_KEY
- AISA_API_KEY
- $AISA_API_KEY

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
