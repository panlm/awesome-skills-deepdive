# Free Groq Voice Recognition

> FREE voice recognition using Groq's complimentary Whisper API. Transcribe audio messages to text in 50+ languages at no cost. Perfect for voice-to-text automation, meeting transcriptions, and accessibility features. Requires free Groq API key.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Free Groq Voice Recognition |
| **作者** | huixionghexiyi |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/huixionghexiyi-free-groq-voice |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/huixionghexiyi/free-groq-voice |
| **安全评级** | 🟢 Low |

## 功能概述
- API Key: gsk_your_key_here
- Model: whisper-large-v3
- Proxy: http://127.0.0.1:7890 (if needed)
- Groq API key (FREE)
- Proxy (if in restricted regions)
- Bash shell (macOS/Linux)

## 使用场景
- 音频内容播放和管理
- 文本转语音功能
- 音乐库搜索和控制

## 依赖和前提条件
- macOS

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `transcribe.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23