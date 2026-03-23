# Voice To Text

> 语音转文字识别工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Voice To Text |
| **作者** | vae999 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/vae999-voice-to-text |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vae999/voice-to-text |
| **安全评级** | 🟡 Medium |

## 功能概述
- MP3, WAV, M4A, OGG, FLAC, AAC, WEBM
- Voice messages from WeChat, Telegram, WhatsApp, etc
- No model found: Download a model to `~/.vosk/models/`
- ffmpeg not found: Install via `brew install ffmpeg` or `apt install ffmpeg`
- Poor accuracy: Try a larger model for better results
- Works completely offline after model download
- Supports multiple languages (download appropriate model)
- Audio is converted to 16kHz mono WAV for processing

## 使用场景
- 将语音录音转换为文本
- 支持多语言语音识别
- 批量处理语音转文字任务

## 依赖和前提条件
- Python / pip
- macOS
- Homebrew

## 包含文件
- `SKILL.md`
- `_meta.json`
- `transcribe.py`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
