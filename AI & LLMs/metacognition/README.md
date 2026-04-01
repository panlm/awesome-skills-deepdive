# metacognition

> Self-reflection engine for AI agents. Extracts patterns from session transcripts into a weighted graph with Hebbian learning and time decay. Compiles a token-budgeted lens of active self-knowledge.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | metacognition |
| **作者** | meimakes |
| **ClawHub** | https://clawskills.sh/skills/meimakes-metacognition |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/meimakes/metacognition |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Maintains a store of categorized insights (perceptions, overrides, protections, self-observations, decisions, curiosities)
- Uses Hebbian reinforcement: repeated insights get stronger, unused ones decay
- Builds a graph of connections between related insights
- Finds clusters of related knowledge that may represent higher-level principles
- Compiles a "metacognition lens" — a token-budgeted summary of active self-knowledge

## 依赖和前提条件

- `LENS_TOKEN

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 检测到: subprocess |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 命令执行。 另有 1 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
