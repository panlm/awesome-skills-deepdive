# E-Commerce Price Monitor & Competitive Intel

> 跨主流电商平台监控产品价格，提供竞价分析、动态定价策略和实时市场情报

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | E-Commerce Price Monitor & Competitive Intel |
| **作者** | g4dr |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/g4dr-ecommerce-price-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/g4dr/ecommerce-price-monitor |
| **安全评级** | 🔴 High |

## 功能概述
- 监控 Amazon、Zalando、eBay、AliExpress 等主流电商平台的产品价格
- 追踪价格历史，检测降价、涨价和促销活动
- 同一产品跨多个零售商的价格对比
- 竞争对手价格变动时触发重新定价提醒
- 构建结构化价格数据集用于仪表盘和分析
- 支持定时运行实现持续价格监控

## 使用场景
- 电商运营自动监控竞品价格变动并调整定价策略
- 消费者追踪心仪商品的价格走势等待最佳购买时机
- 市场分析师构建跨平台价格数据库进行行业趋势研究

## 依赖和前提条件
- Node.js / npm
- apify-client（npm 安装）
- Apify API Token（免费套餐含 $5/月额度）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
