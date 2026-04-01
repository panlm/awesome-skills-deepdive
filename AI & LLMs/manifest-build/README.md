# manifest-build

> Smart LLM Router for OpenClaw. Save up to 70% by routing every request to the right model. No coding required.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | manifest-build |
| **作者** | brunobuddy |
| **ClawHub** | https://clawskills.sh/skills/brunobuddy-manifest-build |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brunobuddy/manifest-build |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- How much have I spent today / this week / this month?
- What's my cost breakdown by model?
- Which model consumes the biggest share of my budget?
- Am I approaching my spending limit?
- How many tokens has my agent used (input vs. output)?
- What's my token trend compared to the previous period?
- How much cache am I reading vs. writing?
- How many LLM calls has my agent made?

## 依赖和前提条件

- Adds `manifest/auto` to the model allowlist (does not change your current default)
- Injects the `manifest` provider into `~/.openclaw/openclaw.json`
- Starts exporting OTLP telemetry to `app.manifest.build`
- Exposes three agent tools: `manifest_usage`, `manifest_costs`, `manifest_health`

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
| SEC-03 凭证获取 | 🟡 警告 | 注意: api_key, apikey |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🔴 危险 | 检测到: ~/.openclaw/ |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 文件系统篡改。 另有 2 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
