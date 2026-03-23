# Phone Caller

> "Make AI-powered outbound phone calls using ElevenLabs voice + GPT brain + Twilio. Supports one-way pre-recorded messages AND live two-way conversations where the AI listens, thinks, and responds in real-time. Use when asked to call someone, leave a voice message, schedule a morning call, have an AI make a reservation or appointment, run a voice campaign, or set up interactive phone conversations. Requires Twilio + ElevenLabs credentials. Triggers on 'call', 'phone', 'voice message', 'reserve', 'book by phone', 'schedule a call', 'call and tell them'."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Phone Caller |
| **作者** | omerflo |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/omerflo-phone-caller |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/omerflo/phone-caller |
| **安全评级** | 🟡 Medium |

## 功能概述
- Default: Clara `tyepWYJJwJM9TTFIg5U7` — Australian female, warm, clear, professional
- See `references/voices.md` for full curated list with IDs and descriptions
- Twilio trial accounts: Can only call verified numbers. Upgrade or verify numbers at console.twilio.com → Verified Caller
- Audio hosting: Scripts use tmpfiles.org for one-off calls (60 min TTL). For scheduled calls, server.py serves audio at `
- localtunnel: Free, no account needed. ngrok requires a free account + authtoken
- Interactive mode latency: ~3-5s per turn (ElevenLabs TTS + GPT + audio upload). Normal for phone conversations

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm
- Python / pip
- macOS
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23