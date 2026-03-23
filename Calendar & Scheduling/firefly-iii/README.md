# Firefly III

> Manage personal finances via Firefly III API. Use when user asks about budgets, transactions, accounts, categories, piggy banks, subscriptions, recurring transactions, or financial reports. Supports creating, listing, updating transactions; managing accounts and balances; setting budgets; tracking savings goals.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Firefly III |
| **作者** | pushp1997 |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/pushp1997-firefly-iii |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pushp1997/firefly-iii |
| **安全评级** | 🟡 Medium |

## 功能概述
- `FIREFLY_URL`: Base URL (e.g., `https://budget.example.com`)
- `FIREFLY_TOKEN`: Personal Access Token (stored at `~/.firefly_token`)
- `422 Unprocessable Entity`: Check required fields in error response
- `401 Unauthorized`: Token expired or invalid
- `404 Not Found`: Resource doesn't exist
- Use `source_name`/`destination_name` to auto-create expense/revenue accounts

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23