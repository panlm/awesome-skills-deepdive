# clawd-coach

> 创建个性化铁人三项、马拉松和超耐力训练计划，可对接 Strava

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawd-coach |
| **作者** | shiv19 |
| **ClawHub** | https://clawskills.sh/skills/shiv19-clawd-coach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shiv19/clawd-coach |
| **安全评级** | 🟡 Medium |

## 功能概述
- 个性化训练计划生成
- Strava OAuth 集成获取训练历史
- SQLite 数据库存储
- 运动特定训练区间和配速
- 比赛日策略建议
- 周期化训练编排

## 使用场景
- 为运动员制定个性化训练计划
- 分析 Strava 历史数据评估体能
- 赛前准备和配速策略

## 依赖和前提条件
Node.js (npx claude-coach), SQLite

## 包含文件
- `SKILL.md`
- `_meta.json`
- `reference/assessment.md`
- `reference/load-management.md`
- `reference/periodization.md`
- `reference/queries.md`
- `reference/race-day.md`
- `reference/workouts.md`
- `reference/zones.md`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 npx 执行 claude-coach CLI |
| SEC-02 数据外泄 | 🟡 Medium | Strava OAuth 认证和数据拉取 |
| SEC-03 凭证获取 | 🟡 Medium | 需要用户提供 Strava Client ID/Secret |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 npm 包 claude-coach |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建 ~/.claude-coach/coach.db SQLite 数据库 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅读取用户授权的 Strava 数据 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化守护进程 |
| SEC-09 信息采集 | 🟡 Medium | 收集用户运动和体能数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及 OAuth 认证和个人运动数据收集，需用户明确授权

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
