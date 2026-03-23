# Financial Planning

> 财务规划和预算管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Financial Planning |
| **作者** | jk-0001 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/jk-0001-financial-planning |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jk-0001/financial-planning |
| **安全评级** | 🟢 Low |

## 功能概述
- Monthly revenue (average of last 3 months if you have history; projected if pre-revenue)
- Monthly fixed expenses (rent/co-working, tools/subscriptions, insurance, hosting, internet — things that don't change month to month)
- Monthly variable expenses (marketing spend, contractor payments, per-transaction fees, travel — things that fluctuate)
- One-time expenses coming up in the next 6 months (equipment, legal, conferences, annual subscriptions)
- Personal income need (the minimum you need to pay yourself each month to cover personal living costs)
- Marketing budget should be 10-20% of revenue (or a fixed dollar amount if pre-revenue — treat it as an investment with expected ROI)
- Owner salary should be set first, then expenses fit around it. If expenses + salary > revenue, something must be cut or revenue must grow
- Always budget a 10-15% buffer for unexpected costs. Unexpected things always happen

## 使用场景
- 制定个人财务规划和预算
- 分析长期投资和储蓄方案
- 模拟不同财务场景的结果

## 依赖和前提条件
- 参见 SKILL.md 获取详细依赖信息

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
