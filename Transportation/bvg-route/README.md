# BVG (Berliner Verkehrsbetriebe) Route Planner

> "Route planning for Berlin public transport (BVG) using the v6.bvg.transport.rest API. Use when the user asks for: (1) route suggestions between two addresses or stops, (2) live next-departure info for a stop, (3) arrival-time–based journey planning (arrive-by or depart-at). Supports outputting 2–3 options ranked by travel time, transfers, and walking, and returning step-by-step directions and refresh tokens for live updates."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BVG (Berliner Verkehrsbetriebe) Route Planner |
| **作者** | jaysonsantos |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/jaysonsantos-bvg-route |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jaysonsantos/bvg-route |
| **安全评级** | 🟢 Low |

## 功能概述
- Provide concise, actionable public-transport directions in Berlin using the v6.bvg.transport.rest API.
- User asks for directions between two places in Berlin (addresses, stop names, or coordinates).
- User asks for next departures from a stop/station.
- User requests to arrive by a specific time (arrive-by) or depart at a specific time.
- Human-readable routes with departure times, transfers, walking distances, estimated arrival, and concise step list.
- Machine-friendly JSON (optional) containing journey id, refreshToken, legs, and stop IDs for programmatic refreshes.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；混淆/反分析：使用编码/解码操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23