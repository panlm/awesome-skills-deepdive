# A nach B - AT Public Transport Service (VOR)

> Austrian public transport (VOR AnachB) for all of Austria. Query real-time departures, search stations/stops, plan routes between locations, and check service disruptions. Use when asking about Austrian trains, buses, trams, metro (U-Bahn), or directions involving public transport in Austria.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | A nach B - AT Public Transport Service (VOR) |
| **作者** | manmal |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/manmal-a-nach-b |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/manmal/a-nach-b |
| **安全评级** | 🟢 Low |

## 功能概述
- `name`: Station name
- `extId`: Station ID for use in other queries
- `type`: S (Station), A (Address), P (POI)
- `coordinates`: WGS84 coordinates (lon/lat in 1e-6 format)
- `line`: Line name (U1, S1, RJ, etc.)
- `direction`: Final destination

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `departures.sh`
- `disruptions.sh`
- `route.sh`
- `search.sh`

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
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23