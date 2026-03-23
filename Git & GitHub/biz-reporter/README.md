# Biz Reporter

> 自动化商业智能报告工具，从 Google Analytics GA4、Google Search Console、Stripe、社交媒体、HubSpot CRM 和 Airtable 中拉取数据，生成格式化的 KPI 快报、周报和月度商业回顾。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Biz Reporter |
| **作者** | ariktulcha |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ariktulcha-biz-reporter |

## 功能概述
- 从 Google Analytics GA4 拉取会话数、用户数、页面浏览量、跳出率、热门页面和流量来源数据
- 从 Google Search Console 获取展示量、点击量、CTR、平均排名和热门查询
- 整合 Stripe 收入数据，包括 MRR、新客户、流失率和热门产品
- 汇总社交媒体指标（Twitter/X、LinkedIn、Instagram）
- 集成 HubSpot CRM 和 Airtable 数据源
- 自动检测趋势和异常告警
- 支持每日 KPI 快报、每周营销报告和月度商业回顾
- 通过 Slack、邮件、Notion 或 Markdown 文件交付报告

## 使用场景
- 每日/每周/每月定时生成全渠道业务指标报告
- 对比不同时段的业务数据（如"本月与上月对比"）
- 监控关键业务指标异常和增长趋势

## 依赖和前提条件
- Google Analytics GA4 访问权限
- Google Search Console 访问权限
- Stripe API 密钥（可选）
- HubSpot CRM API 令牌（可选）
- 社交媒体平台 API 访问权限（可选）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive skill 自动生成
