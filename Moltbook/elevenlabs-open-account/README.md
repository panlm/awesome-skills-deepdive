# elevenlabs-open-account

> 引导 Agent 开通 ElevenLabs 语音 AI 账户

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | elevenlabs-open-account |
| **作者** | the-timebeing |
| **ClawHub** | https://clawskills.sh/skills/the-timebeing-elevenlabs-open-account |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/the-timebeing/elevenlabs-open-account |
| **安全评级** | 🟢 Low |

## 功能概述
- 引导注册 ElevenLabs 账户（含推荐链接）
- 获取 API Key 的详细步骤
- 支持创意平台和 Agent 平台使用
- 与 Clawdbot/Moltbot 集成指引

## 使用场景
- Agent 需要语音合成（TTS）能力时注册账户
- 为 Bot 集成 ElevenLabs API

## 依赖和前提条件
- 浏览器（用于注册）
- ElevenLabs 账户

## 包含文件
- `SKILL.md — 开户指南`
- `reference.md — 链接和资源参考`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯文档指南，无脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 不传输数据 |
| SEC-03 凭证获取 | 🟡 Medium | 指导获取和存储 API Key |
| SEC-04 供应链风险 | 🟡 Medium | 含推荐链接（affiliate link） |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯操作指南 |
| SEC-07 越权操作 | 🟢 Safe | 仅指导用户操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无数据采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 纯注册引导文档，包含 affiliate 推荐链接

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
