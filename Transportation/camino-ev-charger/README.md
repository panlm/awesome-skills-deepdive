# Ev Charger Locations

> "Find EV charging stations along a route or near a destination using Camino AI's location intelligence with OpenStreetMap data."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ev Charger Locations |
| **作者** | james-southendsolutions |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/james-southendsolutions-camino-ev-charger |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-ev-charger |
| **安全评级** | 🟡 Medium |

## 功能概述
- Use a larger radius (5000-10000m) since EV chargers are less densely distributed than other amenities
- Include the charger network name in the query if you need a specific one (e.g., "Tesla Supercharger", "ChargePoint")
- Combine with the `route` skill to plan charging stops along a driving route
- Combine with the `relationship` skill to check distances from chargers to your destination
- For road trip planning, use the `travel-planner` skill with charging waypoints

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23