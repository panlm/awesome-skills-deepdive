# sequence-cli

> Manage Sequence smart wallets, projects, API keys, ERC20 transfers, and query blockchain data using the Sequence Builder CLI. Use when user asks about creating wallets, sending tokens, checking balances, managing Sequence projects, or interacting with EVM blockchains.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | sequence-cli |
| **作者** | jameslawton |
| **ClawHub** | https://clawskills.sh/skills/jameslawton-sequence-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jameslawton/sequence-cli |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Node.js 18+
- A Sequence Builder account (created automatically on first login)
- **EOA Address** — Standard Ethereum address from your private key. Used for login and project ownership.
- **Sequence Wallet Address** — Smart contract wallet that can pay gas fees with ERC20 tokens (no native token needed). Used for transfers.
- `-k, --private-key <key>` — Wallet private key (optional if stored)
- `-a, --access-key <key>` — Project access key (required)

## 依赖和前提条件

- Node.js 18+
- A Sequence Builder account (created automatically on first login)

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
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: apikey, api key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🟡 警告 | 注意: list all |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 5 项警告: 命令执行, 凭证获取, Prompt 注入, 越权操作, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
