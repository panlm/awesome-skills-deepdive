# KallyAI Executive Assistant

> "KallyAI Executive Assistant — AI that handles phone calls (outbound + inbound), email, bookings, research, errands, multi-channel messaging, and phone number management on your behalf. Use when users want to: make/receive calls, manage inbound rules, handle voicemails, provision phone numbers, send email, book restaurants/hotels, search for services, manage calendar, check inbox/messages, handle bills, order food/rides, run errands, check credits/budget, coordinate goals, manage channels (WhatsApp/Telegram/social), run outreach campaigns, referrals, or any delegation task."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | KallyAI Executive Assistant |
| **作者** | sltelitsyn |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/sltelitsyn-kallyai |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sltelitsyn/kallyai |
| **安全评级** | 🟡 Medium |

## 功能概述
- Token storage: `~/.kallyai_token.json` with 0600 permissions
- CSRF protection: State parameter validation
- Localhost only: OAuth redirects only to localhost/127.0.0.1
- Auto-refresh: Tokens refresh automatically when expired

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23