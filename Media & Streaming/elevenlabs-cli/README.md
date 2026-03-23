# ElevenLabs CLI

> ElevenLabs 语音合成命令行工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ElevenLabs CLI |
| **作者** | hongkongkiwi |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/hongkongkiwi-elevenlabs-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hongkongkiwi/elevenlabs-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- API Key: Your ElevenLabs API key is sent only to `api.elevenlabs.io` for authentication
- Audio/Text Content: Text and audio files you process are sent to ElevenLabs API
- No Local Persistence: The CLI does not store your data locally beyond specified output files
- No Telemetry: No usage data is sent to any third party
- ElevenLabs API key - Get one free at ElevenLabs API Keys
- Main Repository: hongkongkiwi/elevenlabs-cli
- Homebrew Tap: hongkongkiwi/homebrew-elevenlabs-cli
- Scoop Bucket: hongkongkiwi/scoop-elevenlabs-cli

## 使用场景
- 通过命令行调用 ElevenLabs TTS
- 管理语音模型和声音库
- 批量生成语音文件

## 依赖和前提条件
- Docker
- macOS
- Homebrew
- API Key

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 安全状态
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
