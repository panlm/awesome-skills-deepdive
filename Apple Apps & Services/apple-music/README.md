# apple-music

> 控制和管理 Apple Music 音乐播放

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | apple-music |
| **作者** | tyler6204 |
| **ClawHub** | https://clawskills.sh/skills/tyler6204-apple-music |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-music |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- 401: Token expired, re-run setup
- 403: Check Apple Music subscription
- 404: Invalid ID or region-locked
- **404 on auth page:** Setup script auto-fixes with HTTP server verification
- **No token in browser:** Restart setup.sh
- **Browser won't open:** Manually open printed URL (Chrome recommended)

## 使用场景

Controls Apple Music through AppleScript for local playback and the MusicKit API for search, library, and playlist management. Local playback works without any setup. API features require an Apple Developer account and a MusicKit key.

## 依赖和前提条件

- macOS 系统
- curl
- Node.js

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: ./apple-music.sh player [now|play|pause|toggle|next|prev|shuffle|repeat|volume N|song "name"], ./apple-music.sh airplay [list|select N|add N|remove N], bash
./launch-setup.sh  # Opens Terminal for interactive setup
 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟡 警告 | 要求用户提供 API 密钥/令牌 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。执行 shell 命令: ./apple-music.sh player [now|play|pau

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
