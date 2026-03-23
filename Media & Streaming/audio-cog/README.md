# audio-cog

> AI audio generation powered by CellCog. Three voice providers (OpenAI, ElevenLabs, MiniMax), avatar cloned voices, sound effects, music generation up to 10 minutes. Professional audio creation with AI.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | audio-cog |
| **作者** | nitishgargiitd |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/nitishgargiitd-audio-cog |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/audio-cog |
| **安全评级** | 🟢 Low |

## 功能概述
- "Warm conversational tone, medium pace, slight enthusiasm when mentioning features. American accent."
- "Deep, hushed, enigmatic, with a slow deliberate cadence — true crime narrator style."
- "Heavy French accent, sophisticated yet friendly, moderate pacing with deliberate pauses."
- The user creates an avatar on cellcog.ai and uploads voice samples
- CellCog clones their voice using MiniMax Speech 2.8 HD
- Any audio request referencing that avatar uses their cloned voice

## 使用场景
- 音频内容播放和管理
- 文本转语音功能
- 音乐库搜索和控制

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23