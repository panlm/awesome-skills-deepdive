# lifi-crosschain

> Cross-chain token swaps and bridges via the LI.FI protocol. Get quotes, execute transfers, track progress, and compose DeFi operations across 35+ blockchains.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | lifi-crosschain |
| **作者** | rhlsthrm |
| **ClawHub** | https://clawskills.sh/skills/rhlsthrm-lifi-crosschain |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rhlsthrm/lifi-crosschain |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- **First positional arg**: Action — `swap`, `bridge`, `track`, `routes`, `zap`, or a natural language request
- **Remaining args**: Details (token names, amounts, chains, tx hashes, etc.)
- **Base URL**: `https://li.quest/v1`
- The API returns `transactionRequest` objects (to, data, value, gasLimit, gasPrice) ready to sign — provide these to the agent's wallet
- **Native token address**: `0x0000000000000000000000000000000000000000` (for ETH, MATIC, BNB, etc.)
- Amounts are always in the token's **smallest unit** (wei): 1 ETH = `1000000000000000000` (18 decimals), 1 USDC = `1000000` (6 decimals)

## 依赖和前提条件

- {"openclaw":{"emoji":"🔗","requires":{"bins":["curl"]},"primaryEnv":"LIFI_API_KEY
- `LIFI_API_KEY

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
