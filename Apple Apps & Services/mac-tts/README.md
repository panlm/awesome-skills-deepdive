# mac-tts

> 使用 macOS 内置 say 命令进行文字转语音

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | mac-tts |
| **作者** | kalijason |
| **ClawHub** | https://clawskills.sh/skills/kalijason-mac-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kalijason/mac-tts |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- **通知**: `say -v "Meijia" "外送到了"`
- **提醒**: `say -v "Meijia" "會議即將開始"`
- **警告**: `say -v "Meijia" "注意，有新的緊急訊息"`
- Runs synchronously (blocks until speech completes)
- Add `&` for async: `say "message" &`
- Works only on macOS

## 使用场景

Wraps the macOS built-in `say` command to produce text-to-speech audio through system speakers. Supports voice selection across multiple languages including English, Mandarin, and Japanese. Volume control is handled via osascript.

## 依赖和前提条件

- macOS (AppleScript)

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
