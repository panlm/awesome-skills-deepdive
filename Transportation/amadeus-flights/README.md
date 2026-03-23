# Amadeus Flight Query

> 通过 Amadeus API 查询航班报价、价格、时刻表和可用性信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Amadeus Flight Query |
| **作者** | kirorab |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/kirorab-amadeus-flights |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kirorab/amadeus-flights |
| **安全评级** | 🟡 Medium |

## 功能概述
- 搜索指定航线的航班报价和价格
- 查询航班时刻表和座位可用性
- 支持多城市、往返和单程搜索
- 获取航空公司和机型信息
- 按价格、时间、经停次数等条件筛选

## 使用场景
- 搜索北京到纽约的最优价格航班
- 比较不同航空公司的经济舱和商务舱价格
- 查询特定日期的航班时刻和可用座位数

## 依赖和前提条件
- API Key（Amadeus Self-Service API）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
