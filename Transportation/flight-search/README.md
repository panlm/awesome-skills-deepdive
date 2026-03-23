# Flight Search

> 搜索 Google Flights 获取航班价格、时间和航空公司信息，无需 API Key

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Flight Search |
| **作者** | awlevin |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/awlevin-flight-search |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/awlevin/flight-search |
| **安全评级** | 🟡 Medium |

## 功能概述
- 搜索指定航线的航班价格和时间
- 比较不同航空公司的报价
- 无需 API Key 即可使用
- 获取直飞和经停航班信息

## 使用场景
- 搜索最便宜的北京到东京航班
- 比较不同日期同一航线的价格差异

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
