# Skill

> Banking interface for AI bots and automation. Get a bank account, issue a Mastercard, buy and sell crypto, send payments and invoices — all via API. Use when the user needs a bank account for a bot, wants to manage balances, make transfers, handle payouts, or operate cards.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | maay |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/maay-brighty |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/maay/brighty |
| **安全评级** | 🔴 High |

## 功能概述
- Crypto account
- EUR / USD / GBP fiat account for self-transfers only (no third-party payments)
- Mastercard virtual card issuance (linked to crypto or fiat accounts)
- Telegram: [@DonatasSupportBot](https://t.me/DonatasSupportBot)
- Email: support@brighty.app
- Never store API key in SKILL.md, memory files, or chat history

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23