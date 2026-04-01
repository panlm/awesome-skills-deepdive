# astrai-inference-router

> Route all LLM calls through Astrai for 40%+ cost savings with intelligent routing and privacy controls

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | astrai-inference-router |
| **作者** | beee003 |
| **ClawHub** | https://clawskills.sh/skills/beee003-astrai-inference-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/beee003/astrai-inference-router |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- **Smart routing**: Classifies each task (code, research, chat, creative) and picks the optimal model
- **Cost savings**: Bayesian learning finds the cheapest provider that meets your quality threshold
- **Auto-failover**: Circuit breaker switches providers when one goes down
- **PII protection**: Personally identifiable information stripped before reaching any provider
- **EU routing**: GDPR-compliant European-only routing with one setting
- **Budget caps**: Set daily spend limits to prevent runaway costs
- **Real-time tracking**: See exactly how much you're saving per request

## 依赖和前提条件

- ["ASTRAI_API_KEY
- "ANTHROPIC_API_KEY
- "ASTRAI_API_KEY

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 未检测到命令执行相关风险模式 |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 1 项警告: 凭证获取。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
