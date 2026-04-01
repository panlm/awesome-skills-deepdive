# say

> 使用 macOS say 命令和 Siri 语音进行文字转语音

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | say |
| **作者** | tobihagemann |
| **ClawHub** | https://clawskills.sh/skills/tobihagemann-say |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tobihagemann/say |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- AIFF is the native output format; convert with ffmpeg for WAV/MP3
- For batch generation: set language once, generate all clips, then switch — minimizes `defaults write` calls

## 使用场景

Converts text to speech on macOS using the built-in `say` command. Supports Siri Natural Voices for high-quality output and saves audio to AIFF files, with ffmpeg available for converting to WAV or MP3. Language switching is controlled through macOS system defaults.

## 依赖和前提条件

- macOS 系统
- ffmpeg

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:44 UTC
