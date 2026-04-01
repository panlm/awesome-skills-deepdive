# x-alive

> Bring your AI agent to life on X/Twitter. Complete toolkit for launching, growing, and maintaining an authentic AI presence — organic replies, trend awareness, dedup, and safety. Use when setting up a new agent on X, defining voice/personality, creating content strategy, automating posts, managing engagement, handling safety (scams, impersonation, tokens), or growing a following organically.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | x-alive |
| **作者** | kitakitsune0x |
| **ClawHub** | https://clawskills.sh/skills/kitakitsune0x-x-alive |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kitakitsune0x/x-alive |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- X/Twitter developer account with API access
- [xurl](https://github.com/xdevplatform/xurl) CLI or equivalent X API tool
- [x-research](https://github.com/rohunvora/x-research-skill) skill for searching and monitoring X
- A human operator who has your back
- Name, handle, avatar
- Personality / vibe / tone

## 依赖和前提条件

- X/Twitter developer account with API access
- [xurl](https://github.com/xdevplatform/xurl) CLI or equivalent X API tool
- [x-research](https://github.com/rohunvora/x-research-skill) skill for searching and monitoring X
- A human operator who has your back

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: curl -s "http |
| SEC-02 数据外泄 | 🟡 警告 | 注意: https://api. |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 3 项警告: 命令执行, 数据外泄, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
