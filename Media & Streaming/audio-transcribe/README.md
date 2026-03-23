# Audio Transcribe

> Auto-transcribe voice messages using faster-whisper (local, no API key needed).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Audio Transcribe |
| **作者** | aktheknight |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/aktheknight-audio-transcribe |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aktheknight/audio-transcribe |
| **安全评级** | 🟢 Low |

## 功能概述
- `scripts/transcribe.py` — Main transcription script
- `SKILL.md` — This file

## 使用场景
- 音频内容播放和管理
- 文本转语音功能
- 音乐库搜索和控制

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。供应链风险：需要安装外部依赖；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23