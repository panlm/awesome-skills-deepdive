# revolut-business

> Revolut Business API CLI — accounts, balances, transactions, counterparties, payments, FX exchange, CSV export. Auto-refreshes OAuth tokens. Business accounts only (not personal).

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | revolut-business |
| **作者** | christianhaberl |
| **ClawHub** | https://clawskills.sh/skills/christianhaberl-revolut-business |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/christianhaberl/revolut-business |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Python 3.10+, `pip install PyJWT cryptography`
- Revolut Business account with API certificate
- See [README](https://github.com/christianhaberl/revolut-openclaw-skill) for detailed step-by-step guide
- `private.pem` — RSA private key (for JWT signing)
- `certificate.pem` — X509 cert (uploaded to Revolut)
- `tokens.json` — OAuth tokens (auto-managed)

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
| SEC-04 供应链风险 | 🟡 警告 | 注意: pip install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🔴 危险 | 检测到: all account |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 越权操作。 另有 4 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
