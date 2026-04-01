# mac-notes-agent

> 通过 agent 管理 Apple Notes 笔记

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | mac-notes-agent |
| **作者** | swancho |
| **ClawHub** | https://clawskills.sh/skills/swancho-mac-notes-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/swancho/mac-notes-agent |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- Lists notes in the given folder (or all folders if omitted).
- Output is JSON array with `title`, `folder`, `creationDate`, and synthetic `id`.
- Replaces the entire body of the matching note.
- Can also use `--id` for identification.
- Appends new content to the end of the existing note.
- Searches note titles and bodies for the keyword.
- Primary key: `(folderName, title)`
- Synthetic ID: `folderName::creationDate::title`

## 使用场景

Connects an AI agent to Apple Notes on macOS using AppleScript through a small Node.js CLI. Supports creating, listing, reading, updating, appending, deleting, and searching notes, with optional folder targeting.

## 依赖和前提条件

- Node.js
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
