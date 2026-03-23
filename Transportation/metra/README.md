# Metra Skill

> Chicago Metra commuter rail — real-time train arrivals, vehicle tracking, service alerts, and schedule info for all 11 Metra lines serving the Chicago metropolitan area. Use when the user asks about Metra trains, Chicago commuter rail, or specific Metra lines and stations.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Metra Skill |
| **作者** | brianleach |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/brianleach-metra |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianleach/metra |
| **安全评级** | 🟡 Medium |

## 功能概述
- Real-time train arrivals — know exactly when the next train arrives at your station
- Live vehicle tracking — see where trains are on the line right now
- Service alerts — know about delays, construction, and service changes before you leave
- Today's schedule — see all remaining trains with inbound/outbound grouping
- Fare calculation — know exactly how much a trip costs between any two stations
- Stop and route lookup — find stations, explore line stops, locate nearby stations

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23