# mnemon

> Persistent memory CLI for LLM agents. Store facts, recall past knowledge, link related memories, manage lifecycle.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | mnemon |
| **作者** | grivn |
| **ClawHub** | https://clawskills.sh/skills/grivn-mnemon |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/grivn/mnemon |
| **安全评级** | 🔴 High (高风险) |

## 功能概述

- id: "brew"
- **Skill** → `~/.openclaw/skills/mnemon/SKILL.md`
- **Hook** → `~/.openclaw/hooks/mnemon-prime/` (agent:bootstrap — injects behavioral guide)
- **Plugin** → `~/.openclaw/extensions/mnemon/` (remind, nudge, compact hooks)
- **Prompts** → `~/.mnemon/prompt/` (guide.md, skill.md)
- Diff is built-in: duplicates skipped, conflicts auto-replaced.

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
| SEC-01 命令执行 | 🔴 危险 | 检测到: exec |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: password |
| SEC-04 供应链风险 | 🟡 警告 | 注意: brew install, go install |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: ~/.openclaw/ |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🔴 High (高风险)**

**风险摘要:** 检测到以下高风险项: 命令执行, 文件系统篡改。 另有 3 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
