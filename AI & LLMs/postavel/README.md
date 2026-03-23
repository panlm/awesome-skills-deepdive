# Postavel

> Connect to Postavel social media management platform via MCP (Model Context Protocol). Create, schedule, and manage social media posts across Facebook, Instagram, and LinkedIn. Use when the user wants to manage social media content, create posts, schedule content, view their content calendar, or interact with their Postavel account through natural language. Activate when user mentions "Postavel", "social media", "schedule post", "create post", "content calendar", or wants to post to Facebook, Instagram, or LinkedIn via their Postavel account.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Postavel |
| **作者** | nezaboravi |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/nezaboravi-postavel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nezaboravi/postavel |
| **安全评级** | 🔴 High |

## 功能概述
- Connect to Postavel via MCP with OAuth authentication
- List workspaces, clients, and brands
- Create and schedule posts across Facebook, Instagram, and LinkedIn
- Manage approval workflows
- View content calendars and post statuses
- The browser auth worked but mcporter didn't detect it

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- macOS
- Homebrew
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23