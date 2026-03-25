# AnachB (奥地利公共交通查询)

> 奥地利公共交通 (VOR AnachB) 查询 — 实时出发信息、路线规划、车站搜索、服务中断查询

## 📖 描述

VOR AnachB 是一个查询奥地利公共交通信息的 skill，通过 HAFAS API 提供实时出发时间、路线规划和服务中断信息。覆盖奥地利全境的火车、公交车、有轨电车、地铁 (U-Bahn) 和城际铁路 (S-Bahn)。

## ✨ 功能特点

- **车站搜索**: 按名称查找车站/停靠站
- **实时出发信息**: 查询车站实时出发时刻
- **路线规划**: 规划两地之间的公共交通路线
- **服务中断查询**: 查看当前运营中断和延误信息
- **全奥地利覆盖**: 支持所有公共交通类型

## 🚀 使用方法

### 安装
```bash
clawhub install manmal/a-nach-b
```

### 脚本概览

| 脚本 | 用途 |
|------|------|
| `search.sh` | 按名称搜索车站 |
| `departures.sh` | 查看车站实时出发信息 |
| `route.sh` | 规划两地之间的路线 |
| `disruptions.sh` | 查看当前服务中断 |

### 使用示例
```bash
# 搜索车站
./search.sh "Stephansplatz"
./search.sh "Wien Hauptbahnhof"

# 查看出发信息
./departures.sh <station-id> [count]

# 路线规划
./route.sh <from-id> <to-id>

# 服务中断
./disruptions.sh
```

### API 信息
- **API**: HAFAS (Hacon Fahrplan-Auskunfts-System)
- **端点**: `https://vao.demo.hafas.de/gate`

## 🔒 安全评估

| 项目 | 状态 |
|------|------|
| ClawHub 页面 | [查看](https://clawskills.sh/skills/manmal-a-nach-b) |
| GitHub 源码 | [查看](https://github.com/openclaw/skills/tree/main/skills/manmal/a-nach-b) |
| 安全状态 | ⚠️ 待验证 (Suspicious) |

## 📚 附加资源

- [ClawSkills 页面](https://clawskills.sh/skills/manmal-a-nach-b)
- [GitHub 源码仓库](https://github.com/openclaw/skills/tree/main/skills/manmal/a-nach-b)
- [HAFAS API 文档](https://vao.demo.hafas.de)
- 作者: @manmal
