# Google Calendar

> Interact with Google Calendar via the Google Calendar API – list upcoming events, create new events, update or delete them. Use this skill when you need programmatic access to your calendar from OpenClaw.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Google Calendar |
| **作者** | adrianmiller99 |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/adrianmiller99-google-calendar |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/adrianmiller99/google-calendar |
| **安全评级** | 🟡 Medium |

## 功能概述
- list upcoming events (optionally filtered by time range or query)
- add a new event with title, start/end time, description, location, and attendees
- update an existing event by its ID
- delete an event by its ID
- Google Calendar API reference: https://developers.google.com/calendar/api/v3/reference
- OAuth 2.0 for installed apps: https://developers.google.com/identity/protocols/oauth2/native-app

## 使用场景
- 管理 Google Calendar 事件
- 查询日程与会议安排
- 自动创建和更新日历事件

## 依赖和前提条件
- Python / pip
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23