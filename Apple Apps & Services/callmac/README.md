# callmac

> 在 macOS 上发起和管理电话/FaceTime 通话

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | callmac |
| **作者** | jooey |
| **ClawHub** | https://clawskills.sh/skills/jooey-callmac |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jooey/callmac |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- **English (US):** `en-US-JennyNeural` (friendly), `en-US-AriaNeural` (confident)
- **Chinese (Mandarin):** `zh-CN-XiaoxiaoNeural` (warm), `zh-CN-XiaoyiNeural` (lively)
- **Other languages:** See [VOICES.md](references/VOICES.md) for complete list
- English segments → English neural voice
- Chinese segments → Chinese neural voice
- Other languages → Default or specified voice
- Local playback on Mac using `afplay`
- Loop playback support (1-∞ times)

## 使用场景

Triggers voice announcements on a Mac from a mobile device by sending messages via Telegram or WhatsApp. Uses edge-tts to synthesize speech with automatic Chinese/English language detection, then plays audio locally through macOS. Supports looping, volume control, and scheduled playback.

## 依赖和前提条件

- Homebrew: ffmpeg
- ffmpeg
- Python 3
- macOS (AppleScript)

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
# Generate and play a simple announcement
python3 scripts/generate_tts.py --text "Hello world" --play

# Generate mixed Chinese/English content
python3 scripts/generate_tts.py --text "Hello 你好" --play

# Save to file
python3 scripts/generate_tts.py --text "Your message" --output announcement.mp3
, 

### Voice Selection

Edge TTS provides high-quality neural voices:
- **English (US):** ,  (lively)
- **Other languages:** See [VOICES.md](references/VOICES.md) for complete list

## Features

### 1. Mixed Language Support
Automatically detects language segments and uses appropriate voices:
- English segments → English neural voice
- Chinese segments → Chinese neural voice
- Other languages → Default or specified voice

### 2. Playback Control
- Local playback on Mac using  |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟡 警告 | 安装软件包: ffmpeg |
| SEC-05 文件系统篡改 | 🔴 危险 | 修改 shell 配置或系统文件 |
| SEC-06 Prompt 注入 | 🟡 警告 | 包含自动执行指令，但在合理范围内 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟡 警告 | 提及 crontab 定时任务 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 发现 1 项危险和 4 项警告。主要风险: 修改 shell 配置或系统文件

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
