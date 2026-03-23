# Pocket TTS Complete Documentation

> 轻量级口袋 TTS 语音合成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Pocket TTS Complete Documentation |
| **作者** | leonaaardob |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/leonaaardob-lb-pocket-tts-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leonaaardob/lb-pocket-tts-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 100M parameters - Small model size
- CPU-only - No GPU required
- ~6x real-time - On M4 MacBook Air
- ~200ms latency - To first audio chunk
- Streaming - Generate audio on-the-fly
- Voice cloning - Clone any voice from 3-10s audio
- English only (more languages planned)

## 使用场景
- 快速将文本转换为语音
- 支持多种语音风格和语言
- 轻量级本地语音合成

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `docs`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
