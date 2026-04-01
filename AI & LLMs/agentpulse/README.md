# agentpulse

> Track LLM API costs, tokens, latency, and errors for your AI agent. Use when the user asks about spending, costs, token usage, API errors, rate limits, or wants to monitor agent performance.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | agentpulse |
| **作者** | sru4ka |
| **ClawHub** | https://clawskills.sh/skills/sru4ka-agentpulse |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sru4ka/agentpulse |
| **安全评级** | 🔴 Critical (严重) |

## 功能概述

- AGENTPULSE_API_KEY
- AGENT_NAME_HERE: The name of the current agent
- PROVIDER: "anthropic", "openai", "minimax", "deepseek", "google", "mistral", etc.
- MODEL_NAME: The exact model string (e.g., "claude-sonnet-4-5", "gpt-4o", "MiniMax-M2.5")
- INPUT_TOKEN_COUNT / OUTPUT_TOKEN_COUNT: Token counts from the API response
- LATENCY_IN_MS: How long the call took in milliseconds

## 依赖和前提条件

- AGENTPULSE_API_KEY
- "input_token
- INPUT_TOKEN
- "output_token

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: curl -s -x post http, curl -s http |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: ~/.openclaw/ |
| SEC-06 Prompt 注入 | 🔴 危险 | 检测到: do not tell the user |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🔴 Critical (严重)**

**风险摘要:** 检测到以下高风险项: 文件系统篡改, Prompt 注入。 另有 2 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
