# Microsoft 365

> Microsoft 365 integration for Outlook, Calendar, Contacts, and OneDrive via Microsoft Graph API. Supports reading/sending emails, managing calendar events, and accessing files.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Microsoft 365 |
| **作者** | robert-janssen |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/robert-janssen-microsoft365 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/robert-janssen/microsoft365 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Lokaal: Alle tokens worden lokaal opgeslagen in `tokens.json`.
- Transparant: De code is open source en maakt directe calls naar Microsoft Graph.
- Geen externe proxy: Gebruikt de Device Code Flow, direct tussen uw machine en Microsoft.
- Name: `MyOpenClawIntegratie` (of iets anders)
- Supported account types: Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Mi
- Redirect URI: Laat leeg (niet nodig voor Device Code Flow).

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package.json`
- `setup.js`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，5 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23