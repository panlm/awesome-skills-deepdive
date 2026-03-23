# Telnyx Tts

> Generate speech audio from text using Telnyx Text-to-Speech API. Use when you need to convert text to spoken audio, create voice messages, or generate audio content.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Telnyx Tts |
| **作者** | teamtelnyx |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/teamtelnyx-telnyx-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teamtelnyx/telnyx-tts |
| **安全评级** | 🟢 Low |

## 功能概述
- `-o, --output PATH`: Output file path (default: output.mp3)
- `--voice VOICE`: Voice ID (default: Telnyx.NaturalHD.astra)
- Telnyx NaturalHD: Premium voices with refined prosody
- `Telnyx.NaturalHD.astra` (default)
- `Telnyx.NaturalHD.luna`
- `Telnyx.NaturalHD.andersen_johan`

## 使用场景
- 音频内容播放和管理
- 文本转语音功能
- 音乐库搜索和控制

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
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