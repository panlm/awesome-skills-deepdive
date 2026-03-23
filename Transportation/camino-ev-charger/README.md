# Ev Charger Locations

> 使用 Camino AI 查找路线沿途或目的地附近的电动汽车充电站

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
- 搜索路线沿途的 EV 充电站
- 查找目的地附近的充电设施
- 获取充电站详情（充电类型、功率、价格）
- 支持多种充电标准筛选

## 使用场景
- 长途驾驶前规划路线上的充电停靠点
- 到达新城市时查找附近可用的快速充电站

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
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
