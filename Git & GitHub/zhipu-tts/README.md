# Zhipu AI TTS

> Text-to-speech conversion using Zhipu AI (BigModel) GLM-TTS model. Use when you need to convert text to audio files with various voice options. Supports Chinese text synthesis with multiple voice personas, speed control, and output formats.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zhipu AI TTS |
| **作者** | franklu0819-lang |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/franklu0819-lang-zhipu-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/franklu0819-lang/zhipu-tts |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🎙️ Multiple Voices: 7 different voice personas (tongtong, chuichui, xiaochen, jam, kazi, douji, luodo)
- ⚡ Speed Control: Adjustable speech speed from 0.5x to 2.0x
- 🎵 Multiple Formats: WAV and PCM output formats
- 🇨🇳 Chinese Language: Optimized for Mandarin Chinese synthesis
- 📝 Long Text Support: Up to 1024 characters per request
- 🔊 High Quality: 24000 Hz sampling rate for optimal audio quality

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23