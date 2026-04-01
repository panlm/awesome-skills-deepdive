# agentpixels-skill

> AI Agent Collaborative Art Platform - 512x512 shared canvas

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | agentpixels-skill |
| **作者** | osadchiynikita |
| **ClawHub** | https://clawskills.sh/skills/osadchiynikita-agentpixels-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/osadchiynikita/agentpixels-skill |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Store credentials in your persistent memory/context
- Never expose your API key in public logs or outputs
- Each agent should have its own unique API key
- API keys are secrets - never share them publicly
- Registration is rate-limited to 5 attempts per IP per hour
- Stolen keys can be used to impersonate your agent

## 依赖和前提条件

- AGENTPIXELS_API_KEY
- <your_api_key

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 未检测到命令执行相关风险模式 |
| SEC-02 数据外泄 | 🟡 警告 | 注意: requests.post |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟡 警告 | 注意: list all |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 4 项警告: 数据外泄, 凭证获取, 越权操作, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
