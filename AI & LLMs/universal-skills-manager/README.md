# universal-skills-manager

> The master coordinator for AI skills. Discovers skills from multiple sources (SkillsMP.com, SkillHub, and ClawHub), manages installation, and synchronization across Claude Code, Gemini CLI, Google Anti-Gravity, OpenCode, and other AI tools. Handles User-level (Global) and Project-level (Local) scopes.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | universal-skills-manager |
| **作者** | jacob-bd |
| **ClawHub** | https://clawskills.sh/skills/jacob-bd-universal-skills-manager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jacob-bd/universal-skills-manager |
| **安全评级** | 🔴 High (高风险) |

## 功能概述

- Wants to **find or search** for new skills.
- Wants to **install** a skill (from a search result or local file).
- Wants to **sync** skills between different AI tools (e.g., "Copy this Gemini skill to OpenCode").
- Asks to **move or copy** skills between scopes (User vs. Project).
- Mentions "Google Anti-Gravity", "OpenCode", or "Gemini" in the context of skills/extensions.
- Wants to **package a skill for claude.ai, Claude Desktop, or ChatGPT** (ZIP upload).

## 依赖和前提条件

- SKILLSMP_API_KEY

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 检测到: | sh |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key, api key |
| SEC-04 供应链风险 | 🔴 危险 | 检测到: curl -fssl https://raw.githubusercontent.com/jacob-bd/universal-skills-manager/main/install.sh | sh |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: ~/.openclaw/, ~/.claude/ |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🔴 危险 | 检测到: admin |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟡 警告 | 注意: encode |

**综合评级: 🔴 High (高风险)**

**风险摘要:** 检测到以下高风险项: 命令执行, 供应链风险, 文件系统篡改, 越权操作。 另有 4 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
