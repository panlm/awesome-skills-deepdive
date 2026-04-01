# claude-usage-checker

> Check Claude Code / Claude Max usage limits. Run when user asks about usage, limits, quota, or how much Claude capacity is left.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | claude-usage-checker |
| **作者** | aligurelli |
| **ClawHub** | https://clawskills.sh/skills/aligurelli-claude-usage-checker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aligurelli/claude-usage-checker |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **Claude CLI** must be installed (`npm i -g @anthropic-ai/claude-code`) and logged in
- If running `claude` shows "Missing API key", the user must log in manually first: open a terminal, run `claude`, and complete the browser login flow
- Requires an interactive PTY — the agent will launch a local process and read its output (quota info only)
- If you see "Missing API key" → tell the user to log in; browser-based login won't work headlessly
- Allow a few seconds between polls — Claude CLI starts slowly
- "Current week" = weekly reset, not daily

## 依赖和前提条件

- **Claude CLI** must be installed (`npm i -g @anthropic-ai/claude-code`) and logged in
- If running `claude` shows "Missing API key", the user must log in manually first: open a terminal, run `claude`, and complete the browser login flow
- Requires an interactive PTY — the agent will launch a local process and read its output (quota info only)

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 检测到: exec |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 命令执行。 另有 1 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
