# pump-fun

> Buy, sell, and launch tokens on Pump.fun using the PumpPortal API

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | pump-fun |
| **作者** | playdadev |
| **ClawHub** | https://clawskills.sh/skills/playdadev-pump-fun |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/playdadev/pump-fun |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- `/pump-buy 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 0.1` - Buy 0.1 SOL worth of tokens
- `/pump-buy 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 0.5 15` - Buy with 15% slippage
- `/pump-sell 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 1000000` - Sell 1,000,000 tokens
- `/pump-sell 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 100%` - Sell all tokens
- `/pump-sell 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 50% 10` - Sell 50% with 10% slippage
- `/pump-launch "My Token" MTK "A revolutionary token" 1` - Launch with 1 SOL dev buy

## 依赖和前提条件

- 无特殊依赖

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
| SEC-04 供应链风险 | 🟡 警告 | 注意: npm install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟡 警告 | 注意: encode |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 4 项警告: 命令执行, 供应链风险, Prompt 注入, 混淆/反分析。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
