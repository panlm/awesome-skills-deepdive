# hergunmac

> 每日 macOS 系统维护和优化任务

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | hergunmac |
| **作者** | ahmetsemsettinozdemirden |
| **ClawHub** | https://clawskills.sh/skills/ahmetsemsettinozdemirden-hergunmac |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ahmetsemsettinozdemirden/hergunmac |
| **安全评级** | 🟢 Safe (安全) |

## 功能概述

- **Match Predictions** with confidence scores (0-100%)
- **Multiple bet types**: Match result, Over/Under, BTTS, Double Chance, Half results
- **Team Statistics**: Form, league position, key players, injuries
- **Head-to-Head Data**: Historical meetings and win/loss breakdown
- **AI Analysis**: Reasoning and key factors for each prediction
- **Maç Sonucu (1X2)**: Home win, Draw, Away win
- **Alt/Üst**: Under/Over goal lines (0.5, 1.5, 2.5, 3.5)
- **Karşılıklı Gol (BTTS)**: Both teams score Yes/No

## 使用场景

Fetches AI-powered football match predictions from hergunmac.com. Returns confidence scores, match result and goal predictions, team statistics, and head-to-head breakdowns for worldwide leagues. Covers upcoming, live, and finished matches.

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 无 shell 命令，或仅使用明确命名的 CLI 工具 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Safe (安全)**

**风险摘要:** 静态分析未发现明显安全问题，但 ClawHub 扫描标记需注意。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
