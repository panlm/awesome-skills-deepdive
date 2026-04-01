# token-alert

> 🚨 **Monitor session tokens and get alerts at 75%/90%/95%**

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | token-alert |
| **作者** | r00tid |
| **ClawHub** | https://clawskills.sh/skills/r00tid-token-alert |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/r00tid/token-alert |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- ✅ **6-Level Threshold System** - Alerts at 25%, 50%, 75%, 90%, 95%, 100%
- ✅ **Material Design Progress Bar** - Box-style (▰/▱) with color gradients
- ✅ **Rich UI Dashboard** - Interactive HTML dashboard with animations
- ✅ **Session Status** - Shows current token usage on demand
- ✅ **Telegram Alerts** - Get notified before hitting limits
- ✅ **HEARTBEAT Integration** - Optional automated checks
- ✅ **Stateless** - No state file needed, calculates on-demand
- ✅ **Session Estimates** - Predicts remaining sessions (~50k avg)

## 依赖和前提条件

- get_session_token

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 2 项警告: 命令执行, Prompt 注入。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
