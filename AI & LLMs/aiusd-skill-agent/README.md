# aiusd-skill-agent

> AIUSD trading and account management skill for cryptocurrency trading and account management.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | aiusd-skill-agent |
| **作者** | chaunceyliu |
| **ClawHub** | https://clawskills.sh/skills/chaunceyliu-aiusd-skill-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chaunceyliu/aiusd-skill-agent |
| **安全评级** | 🔴 High (高风险) |

## 功能概述

- "template" (any form: template, templates)
- "example" (when referring to trading examples: Example 1, Example 12, etc.)
- "pattern" (when referring to trading patterns)
- "using template", "get template", "trading template", "buy template"
- "use Example [number]", "based on template", "following template"
- "skill verification", "verification"

## 依赖和前提条件

- `MCP_HUB_TOKEN

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: curl -l "http, bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: npm install |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: rm -rf |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🔴 危险 | 检测到: all user |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🔴 High (高风险)**

**风险摘要:** 检测到以下高风险项: 文件系统篡改, 越权操作。 另有 3 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
