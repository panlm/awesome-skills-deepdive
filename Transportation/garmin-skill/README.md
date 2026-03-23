# Garmin Skill

> 与 Garmin 运动数据对话，查询活动记录、训练负荷、VO2 Max 等指标

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Garmin Skill |
| **作者** | nftechie |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/nftechie-garmin-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nftechie/garmin-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询 Garmin 设备记录的运动活动数据
- 获取训练负荷和恢复状态指标
- 查看 VO2 Max 和体能趋势
- 分析运动表现和进步趋势
- 支持自然语言查询运动数据

## 使用场景
- 查询本周的跑步数据和训练负荷
- 了解近期 VO2 Max 变化趋势
- 分析过去一个月的运动表现数据

## 依赖和前提条件
- Garmin Connect 账号、API Key

## 安全状态
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

> 本文档由 awesome-skills-deepdive skill 自动生成
