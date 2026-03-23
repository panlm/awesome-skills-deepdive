# gcal-pro - Google Calendar

> Google Calendar integration for viewing, creating, and managing calendar events. Use when the user asks about their schedule, wants to add/edit/delete events, check availability, or needs a morning brief. Supports natural language like "What's on my calendar tomorrow?" or "Schedule lunch with Alex at noon Friday." Free tier provides read access; Pro tier ($12) adds create/edit/delete and morning briefs.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gcal-pro - Google Calendar |
| **作者** | bilalmohamed187-cpu |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/bilalmohamed187-cpu-gcal-pro |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bilalmohamed187-cpu/gcal-pro |
| **安全评级** | 🟡 Medium |

## 功能概述
- ✅ View today's events
- ✅ View tomorrow / this week
- ✅ Search events
- ✅ List calendars
- ✅ Find free time slots
- ✅ Everything in Free

## 使用场景
- 管理 Google Calendar 事件
- 查询日程与会议安排
- 自动创建和更新日历事件

## 依赖和前提条件
- Python / pip
- OAuth

## 包含文件
- `ORIGINAL_README.md`
- `README-INSTALL.txt`
- `SKILL.md`
- `_meta.json`
- `docs`
- `references`
- `requirements.txt`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。凭证获取：需要多种敏感凭证；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23