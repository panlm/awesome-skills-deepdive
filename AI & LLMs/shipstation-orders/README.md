# ShipStation Orders

> 集成 ShipStation API 自动化物流订单管理和发货跟踪

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ShipStation Orders |
| **作者** | cprice70 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/cprice70-shipstation-orders |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cprice70/shipstation-orders |
| **安全评级** | 🔴 High |

## 功能概述
- 集成 ShipStation API 管理物流订单
- 查询和跟踪发货状态
- 批量处理订单和发货标签
- 获取运费估算和物流方案
- 自动同步订单数据
- 支持多承运商物流管理

## 使用场景
- 电商运营中自动同步和管理物流订单
- 通过 AI 助手查询发货状态和物流信息
- 批量处理跨境电商的多渠道发货需求

## 依赖和前提条件
- Node.js 运行环境
- Bash/Shell 环境
- API Key

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
