# Norman: Tax Report

> Review and manage German tax reports including VAT (Umsatzsteuer), income tax prepayments, and Finanzamt submissions. Use when the user asks about taxes, Steuern, VAT, USt, Finanzamt, or tax filing.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Norman: Tax Report |
| **作者** | stanlee000 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/stanlee000-norman-tax-report |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stanlee000/norman-tax-report |
| **安全评级** | 🟢 Low |

## 功能概述
- norman-finance
- Reporting period
- Revenue and VAT amounts
- Status (draft, ready, submitted)
- Finanzamt submission status
- ALWAYS show a preview before submitting to the Finanzamt

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
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23