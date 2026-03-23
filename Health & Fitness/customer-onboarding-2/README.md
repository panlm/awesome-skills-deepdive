# Customer Onboarding

> Design and execute customer onboarding that drives activation and retention. Use when building onboarding flows for new users, reducing churn in the first 30 days, improving time-to-value, or creating onboarding sequences (email, in-app, or manual). Covers activation metrics, onboarding step design, friction reduction, and measuring onboarding success. Trigger on "customer onboarding", "onboarding flow", "user onboarding", "reduce early churn", "improve activation", "onboarding sequence", "time to value".

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Customer Onboarding |
| **作者** | jk-0001 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/jk-0001-customer-onboarding-2 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jk-0001/customer-onboarding-2 |
| **安全评级** | 🟢 Low |

## 功能概述
- Slack: Sent 2,000 messages as a team
- Dropbox: Uploaded and shared at least one file
- SaaS analytics tool: Connected a data source and viewed their first report
- Project management tool: Created a project and added 3 tasks
- What does the user need to do?
- What's blocking them from doing it? (friction, confusion, missing information)

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23