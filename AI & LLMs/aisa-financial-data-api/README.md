# aisa financial data api

> 查询股票和加密货币的实时及历史金融数据，包括价格、市场动态、指标和趋势，用于分析、预警和报告。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | aisa financial data api |
| **作者** | aisadevco |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/aisadevco-aisa-financial-data-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aisadevco/aisa-financial-data-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- 一个 API 密钥即可访问股票和加密货币全部市场数据
- 支持跨资产组合查询（BTC、ETH 与 AAPL、NVDA 等同时获取）
- 提供投资研究所需的完整数据链（价格趋势、内幕交易、分析师评估、SEC 文件）
- 实时加密货币价格追踪与 30 天历史图表
- 上市公司财报分析和分析师预估对比
- 市场筛选功能（按 P/E 比率、营收增长等指标过滤）
- 大户交易（鲸鱼）监控及与价格走势的关联分析
- 支持灵活的时间间隔查询（秒、分钟、日、周、月、年）

## 使用场景
- 为自主 AI Agent 提供完整的市场数据支持，实现自动化投资决策
- 进行全面的公司基本面分析，结合内幕交易和 SEC 文件数据
- 构建量化交易策略所需的多时间框架数据获取管道

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
