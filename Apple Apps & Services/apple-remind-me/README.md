# apple-remind-me

> 创建和管理 Apple Reminders 提醒事项

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-remind-me |
| **作者** | plgonzalezrx8 |
| **ClawHub** | https://clawskills.sh/skills/plgonzalezrx8-apple-remind-me |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/plgonzalezrx8/apple-remind-me |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- **Backend:** Uses `remindctl` command-line tool (macOS native)
- **Date Parsing:** BSD date utility (macOS compatible)
- **Time Format:** ISO 8601 timestamps for remindctl
- **List Filtering:** Shows only incomplete reminders by default
- **Sync:** All changes sync immediately to iCloud and all devices
- macOS (darwin)
- Apple Reminders.app
- Day of week parsing requires lowercase (e.g., "monday" not "Monday")

## 使用场景

Manages Apple Reminders from natural language input on macOS. Creates, lists, edits, completes, and deletes reminders using shell scripts backed by remindctl. Changes sync immediately to iCloud and all connected Apple devices.

## 依赖和前提条件

- Python 3
- macOS Shortcuts

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
