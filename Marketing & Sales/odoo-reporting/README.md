# Odoo Reporting

> "Query Odoo data including salesperson performance, customer analytics, orders, invoices, CRM, accounting, VAT, inventory, and AR/AP. Generates WhatsApp cards, PDFs, Excel. Use when user explicitly mentions Odoo or asks for Odoo data."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Odoo Reporting |
| **作者** | ashrf-in |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/ashrf-in-odoo-reporting |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ashrf-in/odoo-reporting |
| **安全评级** | 🔴 High |

## 功能概述
- 5 Pre-built Reports: Financial Health, Revenue Analytics, AR/AP Aging, Expense Breakdown, Executive Summary
- Compliant Financial Statements: P&L, Balance Sheet, Cash Flow
- Automatic Standard Detection: Detects company's accounting standard (IFRS, US GAAP, Ind-AS, UK GAAP, SOCPA, CAS, JGAAP, 
- Ad-hoc Builder: Custom comparisons (revenue vs expenses, direct vs indirect, etc.)
- Dual Output: WhatsApp cards (dark theme) + PDF reports (light theme)
- Interactive: Prompts for missing params — no assumptions

## 使用场景
- 营销数据分析和报告
- 绩效指标追踪
- ROI 分析和优化建议

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SECURITY.md`
- `SKILL.md`
- `_meta.json`
- `assets`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23