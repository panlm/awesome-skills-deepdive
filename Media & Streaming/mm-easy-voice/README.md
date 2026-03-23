# mmEasyVoice

> Simple text-to-speech skill using MiniMax Voice API. Converts text to audio with customizable voice selection. Use for generating speech audio from text.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mmEasyVoice |
| **作者** | blue-coconut |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/blue-coconut-mm-easy-voice |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/blue-coconut/mm-easy-voice |
| **安全评级** | 🟡 Medium |

## 功能概述
- MINIMAX_VOICE_API_KEY environment variable (required)
- FFmpeg (optional, for audio merging/conversion)
- `text`: The text you want to convert to speech
- `-o OUTPUT`: Output audio file path (required)
- `-v VOICE_ID`: Voice to use (default: male-qn-qingse)
- Up to 10,000 characters per request

## 使用场景
- 音频内容播放和管理
- 文本转语音功能
- 音乐库搜索和控制

## 依赖和前提条件
- Python / pip
- macOS
- Homebrew
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `check_environment.py`
- `mmvoice.py`
- `reference`
- `requirements.txt`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23