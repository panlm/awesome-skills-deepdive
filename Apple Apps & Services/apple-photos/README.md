# apple-photos

> 管理和搜索 Apple Photos 照片库

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-photos |
| **作者** | tyler6204 |
| **ClawHub** | https://clawskills.sh/skills/tyler6204-apple-photos |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-photos |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- Full Disk Access for terminal (System Settings → Privacy → Full Disk Access)
- Recent/search: `Filename | Date | Type | UUID`
- People: `ID | Name | Photo Count`
- Default export: `/tmp/photo_export.jpg`
- Date format: `YYYY-MM-DD` or `YYYY-MM-DD HH:MM`
- Content search uses ML, slower (~5-10s) than date/person (~100ms)
- HEIC auto-converts to JPEG on export
- Name search is case-insensitive, partial match

## 使用场景

Provides terminal access to macOS Photos.app by querying the Photos SQLite database directly. Supports listing albums and people, searching photos by date range, person name, or visual content, and exporting photos to JPEG.

## 依赖和前提条件

- macOS 系统

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: scripts/photos-count.sh, scripts/photos-list-albums.sh, scripts/photos-recent.sh [count] |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 1 项警告，无严重风险。执行 shell 命令: scripts/photos-count.sh, scripts/phot

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
