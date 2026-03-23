# Windsor.ai Analytics

> Connect to Windsor.ai MCP for natural language access to 325+  data sources including Facebook Ads, GA4, HubSpot, Shopify, and more.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Windsor.ai Analytics |
| **作者** | carlosarturoleon |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/carlosarturoleon-windsor-ai |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/carlosarturoleon/windsor-ai |
| **安全评级** | 🔴 High |

## 功能概述
- Campaign performance, ROAS, CPM, CPC, CTR
- Ad spend breakdowns or budget analysis across channels
- Sales pipeline, CRM data, or customer acquisition metrics
- E-commerce performance (revenue, conversion rates, AOV)
- Cross channel attribution or multi touch analytics
- Trend analysis over specific date ranges

## 使用场景
- 营销数据分析和报告
- 绩效指标追踪
- ROI 分析和优化建议

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23