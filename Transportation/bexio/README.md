# bexio

> Bexio Swiss business software API for managing contacts, quotes/offers, invoices, orders, and items/products. Use when working with Bexio CRM, creating or managing invoices, quotes, sales orders, contact management, or Swiss business administration tasks. Supports listing, searching, creating, editing contacts and sales documents.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | bexio |
| **作者** | rdewolff |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/rdewolff-bexio |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rdewolff/bexio |
| **安全评级** | 🟡 Medium |

## 功能概述
- `contact_show`, `contact_edit` - Contacts
- `kb_offer_show`, `kb_offer_edit` - Quotes/Offers
- `kb_invoice_show`, `kb_invoice_edit` - Invoices
- `kb_order_show`, `kb_order_edit` - Orders
- `article_show` - Items/Products
- Quotes: `draft`, `pending`, `accepted`, `declined`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23