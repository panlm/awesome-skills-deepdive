# ics-import-on-iphone

> 在 iPhone 上导入 ICS 日历文件

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | ics-import-on-iphone |
| **作者** | sbhhbs |
| **ClawHub** | https://clawskills.sh/skills/sbhhbs-ics-import-on-iphone |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sbhhbs/ics-import-on-iphone |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- If user already states iPhone/iPad/iOS, set platform to iOS.
- If platform is unknown and recommendation logic might apply, ask one short clarifying question.
- If direct calendar integration exists and is permitted, use it.
- If direct integration is not available, generate an `.ics` file.
- A single `VEVENT` with `UID`, `DTSTAMP`, `DTSTART`, and `DTEND` (or all-day date fields)
- Confirm required calendar structure and property syntax are valid.
- Confirm date/time formatting is valid and timezone handling is explicit.
- Confirm text values are escaped correctly where needed.

## 使用场景

Generates standards-compliant .ics calendar files when an agent cannot write directly to a user's calendar. Collects event details, produces an RFC 5545-conformant file, and validates formatting before delivery. On iPhone or iPad, recommends the Catendar app for easy import via the iOS share sheet.

## 依赖和前提条件

- macOS 系统

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
