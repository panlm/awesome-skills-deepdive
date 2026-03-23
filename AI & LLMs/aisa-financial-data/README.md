# AIsa Financial Data

> 查询股票和加密货币的实时及历史金融数据，包括价格、市场动态、指标和趋势，用于分析、预警和报告。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AIsa Financial Data |
| **作者** | aisapay |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/aisapay-aisa-financial-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-financial-data |
| **安全评级** | 🟡 Medium |

## 功能概述
- 获取股票历史价格和实时报价数据
- 查询上市公司最新新闻和公告
- 获取财务报表数据（利润表、资产负债表、现金流量表）
- 查看分析师 EPS 预测和投资评级
- 追踪内部人士交易记录
- 查阅 SEC 文件（10-K、10-Q、8-K 等）
- 获取加密货币实时价格和历史数据
- 支持跨资产组合分析（股票 + 加密货币）

## 使用场景
- 构建跨资产投资组合监控面板，同时追踪股票和加密货币
- 进行上市公司深度研究，包括财务报表、内幕交易和分析师评级
- 设置市场价格预警和自动化报告

## 依赖和前提条件
- 需要 `curl` 和 `python3`
- 需要 `AISA_API_KEY` 环境变量

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
