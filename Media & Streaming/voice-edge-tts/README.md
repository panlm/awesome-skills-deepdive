# Voice (Edge TTS)

> Edge TTS 语音合成工具 — 使用微软 Edge 引擎

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Voice (Edge TTS) |
| **作者** | zhaov1976 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/zhaov1976-voice-edge-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zhaov1976/voice-edge-tts |
| **安全评级** | 🟡 Medium |

## 功能概述
- Edge TTS Engine - High quality text-to-speech using Microsoft Edge
- Streaming Playback - Real-time audio streaming (边生成边播放)
- Multiple Voices - Support for Chinese, English, Japanese, Korean voices
- Customizable - Adjust rate, volume, and pitch
- Secure Implementation - No command injection vulnerabilities
- Enterprise-grade security - Full command injection protection
- Voice whitelist validation
- Replaced exec with spawn for secure process execution

## 使用场景
- 使用微软 Edge TTS 生成语音
- 支持多语言和多种声音选择
- 免费的高质量语音合成

## 依赖和前提条件
- Python / pip
- macOS
- Homebrew

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `example.js`
- `index.js`
- `package-lock.json`
- `package.json`
- `skill.json`
- `stream_speak.py`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。命令执行：发现直接命令执行指令；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
