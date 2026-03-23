# Miranda ElevenLabs Speech (TTS/STT)

> 集成 ElevenLabs AI 语音技术，实现高质量文字转语音（TTS）和语音转文字（STT）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Miranda ElevenLabs Speech (TTS/STT) |
| **作者** | jeffpignataro |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jeffpignataro-miranda-elevenlabs-speech |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jeffpignataro/miranda-elevenlabs-speech |
| **安全评级** | 🔴 High |

## 功能概述
- 高质量 AI 文字转语音（TTS）
- 语音转文字（STT）识别
- 多种 AI 语音角色选择
- 自然流畅的语音合成
- 支持多语言语音生成
- 语音克隆和自定义音色

## 使用场景
- 将文章或消息转换为自然语音播报
- 智能体以语音形式与用户交互
- 语音备忘录自动转写为文字

## 依赖和前提条件
- ElevenLabs API 密钥
- ElevenLabs 账户（免费或付费）
- 音频播放/录制设备

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
