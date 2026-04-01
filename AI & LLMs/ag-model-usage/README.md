# ag-model-usage

> Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current (most recent) model or a full model breakdown. Trigger when asked for model-level usage/cost data from codexbar, or when you need a scriptable per-model summary from codexbar cost JSON.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | ag-model-usage |
| **作者** | ls18166407597-design |
| **ClawHub** | https://clawskills.sh/skills/ls18166407597-design-ag-model-usage |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ls18166407597-design/ag-model-usage |
| **安全评级** | 🟢 Safe (安全) |

## 功能概述

- **实时同步**：直接从 Google 内部 API 获取最真实的账户配额数据。
- **状态监控**：支持 Gemini、Claude 等核心模型的剩余额度展示。
- **时间预估**：精准显示每个模型下次刷新的具体时间点（已转换为本地时区）。

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 未检测到命令执行相关风险模式 |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Safe (安全)**

**风险摘要:** 未检测到明显安全风险。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
