# Check and book Tennis and Pickleball Courts at Bay Club Gateway

> "Book and manage tennis/pickleball courts at Bay Club."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Check and book Tennis and Pickleball Courts at Bay Club Gateway |
| **作者** | elizabethsiegle |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/elizabethsiegle-bayclub-gateway-booking |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/elizabethsiegle/bayclub-gateway-booking |
| **安全评级** | 🔴 High |

## 功能概述
- 🎾 Check and book tennis courts
- 🏓 Check and book pickleball courts
- 🤖 Runs browser automation via Stagehand
- 📅 Works with "today", "tomorrow", or specific weekdays
- 💬 WhatsApp interface - just text to book
- 📆 Auto-adds bookings to Google Calendar

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `BayClubBot.ts`
- `GoogleCalendarService.js`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `bayclub_skills.ts`
- `cli.ts`
- `package-lock.json`
- `package.json`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23