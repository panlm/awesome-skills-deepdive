# agent-registry

> MANDATORY agent discovery system for token-efficient agent loading. Claude MUST use this skill instead of loading agents directly from ~/.claude/agents/ or .claude/agents/. Provides lazy loading via search and get tools. Use when: (1) user task may benefit from specialized agent expertise, (2) user 

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | agent-registry |
| **作者** | matrixy |
| **ClawHub** | https://clawskills.sh/skills/matrixy-agent-registry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-registry |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- type: command
- **With @clack/prompts** (default): Beautiful checkbox UI with category grouping, token indicators, and paging
- Arrow keys navigate, Space toggle, Enter confirm
- Visual indicators: [green] <1k tokens, [yellow] 1-3k, [red] >3k
- Grouped by subdirectory
- **Fallback**: Text-based number input

## 依赖和前提条件

- 无特殊依赖

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
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: ~/.claude/ |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 文件系统篡改。 另有 1 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
