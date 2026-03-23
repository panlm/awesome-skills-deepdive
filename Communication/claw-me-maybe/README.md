# Claw Me Maybe - Beeper Desktop API & Multi-Platform Messaging

> Beeper integration for Clawdbot. Send messages and search chats across WhatsApp, Telegram, Signal, Discord, Slack, Instagram, iMessage, LinkedIn, Facebook Messenger, Google Messages via Beeper Desktop API. Reactions, reminders, attachments, mark as read. Unified multi-platform messaging automation—just ask.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Claw Me Maybe - Beeper Desktop API & Multi-Platform Messaging |
| **作者** | nickhamze |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/nickhamze-claw-me-maybe |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nickhamze/claw-me-maybe |
| **安全评级** | 🟡 Medium |

## 功能概述
- [Get Beeper](https://www.beeper.com/download) - Free download
- [Beeper Developer Docs](https://developers.beeper.com) - Full API reference
- [Beeper MCP](https://www.beeper.com/mcp) - For Claude Desktop & Cursor users
- [Beeper Desktop API Reference](https://developers.beeper.com/desktop-api-reference/) - Complete endpoint docs

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- macOS
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23