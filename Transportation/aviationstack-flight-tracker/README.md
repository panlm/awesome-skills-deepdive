# Flight Tracker

> 通过 AviationStack API 实时追踪航班状态、登机口信息和延误详情

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Flight Tracker |
| **作者** | copey02 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/copey02-aviationstack-flight-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/copey02/aviationstack-flight-tracker |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时追踪全球航班状态和位置
- 获取登机口分配和航站楼信息
- 查看航班延误原因和预计时间
- 查询航空公司和航线信息
- 支持按航班号、航线或机场查询

## 使用场景
- 实时追踪正在飞行中的航班位置和预计到达时间
- 查看某机场当日所有出发/到达航班的状态
- 监控航班延误并获取替代方案信息

## 依赖和前提条件
- API Key（AviationStack）

## 安全状态
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

> 本文档由 awesome-skills-deepdive skill 自动生成
