# get-focus-mode

> 获取当前 macOS/iOS 专注模式状态

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | get-focus-mode |
| **作者** | nickchristensen |
| **ClawHub** | https://clawskills.sh/skills/nickchristensen-get-focus-mode |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nickchristensen/get-focus-mode |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- "No Focus" - Focus mode is off
- "Office" - Office focus is active
- "Sleep" - Sleep focus is active
- "Do Not Disturb" - DND is active

## 使用场景

Reads the currently active macOS Focus mode and prints its name to stdout. Returns 'No Focus' when no mode is active, or the mode name (e.g. 'Do Not Disturb', 'Office', 'Sleep') when one is on.

## 依赖和前提条件

- macOS 系统
- jq

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
