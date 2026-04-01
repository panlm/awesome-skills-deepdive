# lieutenant

> AI agent security and trust verification. Scan messages, agent cards, and A2A communications for prompt injection, jailbreaks, and malicious patterns. Use when protecting agents from attacks, verifying external agents, or scanning untrusted content.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | lieutenant |
| **作者** | jd-delatorre |
| **ClawHub** | https://clawskills.sh/skills/jd-delatorre-lieutenant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jd-delatorre/lieutenant |
| **安全评级** | 🔴 Critical (严重) |

## 功能概述

- **65+ threat patterns** across 10 categories
- **Semantic analysis** catches paraphrased attacks (requires OpenAI API key)
- **A2A integration** for agent-to-agent communication protection
- **TrustAgents API** for reputation data and crowdsourced threat intel

## 依赖和前提条件

- OpenAI API key
- OPENAI_API_KEY
- TRUSTAGENTS_API_KEY

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 检测到: eval |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key, password, api key |
| SEC-04 供应链风险 | 🟡 警告 | 注意: pip install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🔴 危险 | 检测到: ignore previous instructions, ignore all previous instructions |
| SEC-07 越权操作 | 🔴 危险 | 检测到: admin |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🔴 Critical (严重)**

**风险摘要:** 检测到以下高风险项: 命令执行, Prompt 注入, 越权操作。 另有 2 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
