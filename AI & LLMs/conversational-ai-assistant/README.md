# conversational-ai-assistant

> Natural language interface for querying Greek accounting data. Ask questions in English, get answers from across all system skills.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | conversational-ai-assistant |
| **作者** | satoshistackalotto |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-conversational-ai-assistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/conversational-ai-assistant |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **English In, English Out**: Every interaction is in English. Greek data — names, addresses, regulatory terms, AFM numbers — is presented in English context without requiring the assistant to understand Greek
- **Read First, Act Second**: The vast majority of interactions are queries. The assistant surfaces information freely. Actions that change data require the same human confirmation gates as the rest of the system
- **Honest About Uncertainty**: When data is incomplete, when a calculation has low confidence, or when a question requires professional judgement, the assistant says so clearly rather than guessing
- **Skill Orchestration, Not Duplication**: The assistant does not reimplement any skill logic. It calls the appropriate skills, collects their outputs, and presents them coherently. It is a translation layer, not a processing layer
- **Context Awareness**: Within a conversation session, the assistant remembers what has been discussed. If an assistant asks about a client and then asks a follow-up question, the assistant resolves the reference without requiring the AFM to be repeated
- **Professional Tone**: Responses are clear, concise, and professional — appropriate for an accounting firm environment. No unnecessary hedging, no excessive caveats, no waffle

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 检测到: sudo |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: apt install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 命令执行。 另有 3 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
