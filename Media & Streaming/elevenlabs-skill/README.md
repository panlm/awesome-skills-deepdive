# ElevenLabs Skill

> Text-to-speech, sound effects, music generation, voice management, and quota checks via the ElevenLabs API. Use when generating audio with ElevenLabs or managing voices.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ElevenLabs Skill |
| **作者** | odrobnik |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/odrobnik-elevenlabs-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/odrobnik/elevenlabs-skill |
| **安全评级** | 🟢 Low |

## 功能概述
- Text-to-Speech: Generate speech using ElevenLabs voices (`speech.py`)
- Sound Effects: Generate sound effects and short clips (`sfx.py`)
- Music Generation: Create musical compositions (`music.py`)
- Voice Management: List voices (`voices.py`) and clone voices (`voiceclone.py`)
- Quota Tracking: Check usage and limits (`quota.py`)

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23