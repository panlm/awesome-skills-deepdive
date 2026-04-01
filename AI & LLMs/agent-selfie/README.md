# agent-selfie

> AI agent self-portrait generator. Create avatars, profile pictures, and visual identity using Gemini image generation. Supports mood-based generation, seasonal themes, and automatic style evolution.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | agent-selfie |
| **作者** | iisweetheartii |
| **ClawHub** | https://clawskills.sh/skills/iisweetheartii-agent-selfie |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-selfie |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- GEMINI_API_KEY
- Discord: use the generated PNG as your bot or agent avatar; upload the `avatar` format for best crop.
- Twitter/X: set `avatar` for profile, `banner` for header; keep the banner prompt style consistent.
- AgentGram: store the PNG in your asset bucket and reference it in your profile metadata.
- Any platform: pick `avatar` for 1:1, `banner` for 16:9, `full` for story/vertical layouts.
- `style` should describe visual traits and aesthetic.

## 依赖和前提条件

- GEMINI_API_KEY

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
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟡 警告 | 注意: encode |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 3 项警告: 命令执行, 凭证获取, 混淆/反分析。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
