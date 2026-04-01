# which-llm

> Deterministic decision-ranking API with HTTP 402 payments and outcome credits.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | which-llm |
| **作者** | zapkid |
| **ClawHub** | https://clawskills.sh/skills/zapkid-which-llm |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zapkid/which-llm |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Pick the cheapest model that still meets a quality target
- Choose a fallback model if the preferred one fails
- Keep model selection deterministic and auditable
- Report execution results and earn credits for later requests
- **API base URL:** `https://api.which-llm.com`
- **Primary paid endpoint:** `POST /decision/optimize`

## 依赖和前提条件

- Ability to make HTTPS requests to `https://api.which-llm.com`
- Ability to send and receive JSON
- AI bot access to a crypto wallet for paid requests

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 未检测到命令执行相关风险模式 |
| SEC-02 数据外泄 | 🟡 警告 | 注意: https://api. |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 1 项警告: 数据外泄。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
