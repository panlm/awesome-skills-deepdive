# crypto-agent-payments

> Create wallets, transfer tokens, and enable payments between agents. Perfect for bug bounty programs, rewards systems, and agent-to-agent transactions.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | crypto-agent-payments |
| **作者** | nicofains1 |
| **ClawHub** | https://clawskills.sh/skills/nicofains1-crypto-agent-payments |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nicofains1/crypto-agent-payments |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **Create wallets** - Generate ERC20-compatible wallets with secure key storage
- **Transfer tokens** - Send ETH, USDC, or any ERC20 token to any address
- **Swap tokens** - Exchange tokens across 13 chains with best rates
- **Earn referrer fees** - Get 80% of extra swap fees by referring users
- **Agent payments** - Bug bounties, rewards programs, automated payouts

## 依赖和前提条件

- 无特殊依赖

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
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: @latest |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 3 项警告: 命令执行, 供应链风险, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
