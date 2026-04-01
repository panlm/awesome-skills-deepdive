# decompose-mcp

> Decompose any text into classified semantic units — authority, risk, attention, entities. No LLM. Deterministic.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | decompose-mcp |
| **作者** | echology-io |
| **ClawHub** | https://clawskills.sh/skills/echology-io-decompose-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/echology-io/decompose-mcp |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **Authority levels** — RFC 2119 keywords: "shall" = mandatory, "should" = directive, "may" = permissive
- **Risk categories** — safety-critical, security, compliance, financial, contractual
- **Attention scoring** — authority weight x risk multiplier, 0-10 scale
- **Standards references** — ASTM, ASCE, IBC, OSHA, ACI, AISC, AWS, ISO, EN
- **Financial values** — dollar amounts, percentages, retainage, liquidated damages
- **Dates** — deadlines, milestones, notice periods
- **Irreducibility** — legal mandates, threshold values, formulas that cannot be paraphrased

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
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟡 警告 | 注意: api key |
| SEC-04 供应链风险 | 🟡 警告 | 注意: pip install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id, hostname |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 4 项警告: 命令执行, 凭证获取, 供应链风险, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
