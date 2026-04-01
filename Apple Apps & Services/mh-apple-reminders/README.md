# mh-apple-reminders

> 管理 Apple Reminders 提醒事项（增强版）

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | mh-apple-reminders |
| **作者** | mohdalhashemi98-hue |
| **ClawHub** | https://clawskills.sh/skills/mohdalhashemi98-hue-mh-apple-reminders |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mohdalhashemi98-hue/mh-apple-reminders |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- User explicitly mentions "reminder" or "Reminders app"
- Creating personal to-dos with due dates that sync to iOS
- Managing Apple Reminders lists
- User wants tasks to appear in their iPhone/iPad Reminders app
- Scheduling Clawdbot tasks or alerts → use `cron` tool with systemEvent instead
- Calendar events or appointments → use Apple Calendar
- Project/work task management → use Notion, GitHub Issues, or task queue
- One-time notifications → use `cron` tool for timed alerts

## 使用场景

Manages Apple Reminders from the terminal using the remindctl CLI. Supports listing, creating, completing, and deleting reminders across named lists with date filters and multiple output formats. Reminders sync to iPhone and iPad through iCloud.

## 依赖和前提条件

- macOS 系统
- Homebrew: steipete/tap/remindctl

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
