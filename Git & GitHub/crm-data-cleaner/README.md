# Crm Data Cleaner

> "Deduplicate, normalize, and enrich CRM contacts and companies. Use when a user needs to clean CRM data, find duplicate contacts, standardize phone numbers or emails, merge duplicate records, audit data quality, or enrich contacts with external sources like Clearbit or Apollo. Works with HubSpot, Salesforce, Pipedrive, or any CRM with CSV export. Instruction-only skill — no scripts or code execution. All operations are performed via CRM platform APIs or CSV export/import workflows."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crm Data Cleaner |
| **作者** | luigi08001 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/luigi08001-crm-data-cleaner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/luigi08001/crm-data-cleaner |
| **安全评级** | 🔴 High |

## 功能概述
- HUBSPOT_ACCESS_TOKEN
- Multiple entries for same person/company
- Slight variations in name spelling
- Different email addresses for same contact
- Incomplete vs. complete records
- Phone numbers: (555) 123-4567 vs 555-123-4567 vs +1.555.123.4567

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23