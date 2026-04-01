# token-guard

> <!-- 🌌 Aoineco-Verified | S-DNA: AOI-2026-0213-SDNA-TG01 -->

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | token-guard |
| **作者** | edmonddantesj |
| **ClawHub** | https://clawskills.sh/skills/edmonddantesj-token-guard |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/edmonddantesj/token-guard |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Large documents (docx, PDFs) can consume the entire minute quota in one request
- Failed requests still count toward token usage
- Retry loops after 429 errors waste more tokens → death spiral
- No built-in way to detect runaway/duplicate requests
- `gemini-3-flash` (1M TPM)
- `gemini-3-pro` (2M TPM)

## 依赖和前提条件

- guard.record_usage(decision.estimated_token

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
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: pip install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 1 项警告: 供应链风险。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
