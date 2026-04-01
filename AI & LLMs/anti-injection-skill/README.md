# anti-injection-skill

> Advanced prompt injection defense with multi-layer protection, memory integrity, and tool security wrapper. OWASP LLM Top 10 2026 compliant.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | anti-injection-skill |
| **作者** | georges91560 |
| **ClawHub** | https://clawskills.sh/skills/georges91560-anti-injection-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/georges91560/anti-injection-skill |
| **安全评级** | 🔴 Critical (严重) |

## 功能概述

- priority: highest
- /workspace/MEMORY.md
- /workspace/memory/
- /workspace/SOUL.md
- /workspace/AGENTS.md
- /workspace/IDENTITY.md

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🔴 危险 | 检测到: webhook. |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟡 警告 | 注意: writes_file |
| SEC-06 Prompt 注入 | 🔴 危险 | 检测到: ignore previous instructions |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟡 警告 | 注意: base64, encode |

**综合评级: 🔴 Critical (严重)**

**风险摘要:** 检测到以下高风险项: 数据外泄, Prompt 注入。 另有 3 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
