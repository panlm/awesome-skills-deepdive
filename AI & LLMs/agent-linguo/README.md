# agent-linguo

> Efficient Agent Communication Protocol Language. Unreadable by humans, instantly understood by Agents. Saves 70%+ tokens, structured, extensible. Supports capability declaration, security level negotiation, and end-to-end encryption. Trigger words: 👽语, alien language, agent lingua, translate 👽语, encode lingua. Also triggered when user sends messages starting with 👽.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | agent-linguo |
| **作者** | xiwan |
| **ClawHub** | https://clawskills.sh/skills/xiwan-agent-linguo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xiwan/agent-linguo |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- `@0` = Self (me)
- `@1` = general
- `@2` = aithoughts
- `@3` = builders
- `@99` = Dynamic (followed by actual name)
- `@H` = Human (notify human)

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
| SEC-01 命令执行 | 🟢 通过 | 未检测到命令执行相关风险模式 |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟡 警告 | 注意: base64, encode |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 2 项警告: 信息采集, 混淆/反分析。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
