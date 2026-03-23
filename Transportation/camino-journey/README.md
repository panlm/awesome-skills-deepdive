# Journey Planning with Waypoints

> 使用 Camino AI 规划多节点行程，支持路线优化和可行性分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Journey Planning with Waypoints |
| **作者** | james-southendsolutions |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/james-southendsolutions-camino-journey |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-journey |
| **安全评级** | 🟡 Medium |

## 功能概述
- 规划包含多个途经点的最优路线
- 行程可行性分析和时间估算
- 支持路线优化和重新排序
- 实时交通数据集成

## 使用场景
- 规划一日多地商务拜访的最优路线
- 评估包含多个景点的旅行路线可行性

## 依赖和前提条件
- API Key（Camino AI）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
