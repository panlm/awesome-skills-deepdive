# Clawhub Skill Passive Income Tracker

> Track all your passive income crypto apps from one place. Unified dashboard showing daily earnings, payout history, and USD/EUR totals across Grass.io, Storj, Mysterium, Honeygain, EarnApp, and more.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Clawhub Skill Passive Income Tracker |
| **作者** | mariusfit |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/mariusfit-passive-income-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mariusfit/passive-income-tracker |
| **安全评级** | 🟡 Medium |

## 功能概述
- Unified earnings dashboard — all apps in one view
- Daily/weekly summaries — automatically messaged to WhatsApp/Telegram
- Payout tracking — logs confirmed payouts and estimates pending rewards
- USD/EUR conversion — fetches live crypto prices for fiat estimates
- Uptime correlation — cross-checks earnings with service uptime
- Alert on low earnings — warns if an app stops earning (node down?)
- CSV/JSON export — for spreadsheet or tax reporting

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Node.js / npm
- Python / pip
- Docker
- API Key
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23