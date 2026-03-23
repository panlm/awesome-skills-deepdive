# A simple Flight Tracker

> 使用 OpenSky Network 实时追踪航班，支持按区域、呼号或机场搜索

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | A simple Flight Tracker |
| **作者** | xenofex7 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/xenofex7-flight-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xenofex7/flight-tracker |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 OpenSky Network 实时追踪航班位置
- 按区域（国家/城市）筛选飞行中的航班
- 按呼号追踪特定航班
- 搜索机场出发/到达的航班时刻
- 获取飞行器详细信息（机型、高度、速度）

## 使用场景
- 查看瑞士上空正在飞行的所有航班
- 追踪特定呼号航班的实时位置和轨迹
- 查询苏黎世机场的实时到达航班列表

## 依赖和前提条件
- Python / pip、API Key（OpenSky Network）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
