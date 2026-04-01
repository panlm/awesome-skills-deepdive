# skill-email-management

> 管理和自动化 Apple Mail 邮件处理

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | skill-email-management |
| **作者** | latisen |
| **ClawHub** | https://clawskills.sh/skills/latisen-skill-email-management |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/latisen/skill-email-management |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- **Overview & Discovery**: `get_inbox_overview`, `list_accounts`, `list_mailboxes`
- **Reading & Searching**: `list_inbox_emails`, `get_recent_emails`, `get_email_with_content`, `search_emails`, `get_email_thread`
- **Composing & Responding**: `compose_email`, `reply_to_email`, `forward_email`
- **Organization**: `move_email`, `update_email_status` (read/unread, flag/unflag)
- **Drafts**: `manage_drafts` (list, create, send, delete)
- **Attachments**: `list_email_attachments`, `save_email_attachment`
- **Analytics**: `get_statistics` (account overview, sender stats, mailbox breakdown)
- **Cleanup**: `manage_trash` (move to trash, delete permanently, empty trash)

## 使用场景

Email management assistant for Apple Mail. Helps users triage, organize, and search their inbox using Apple Mail MCP tools. Covers workflows from daily triage to bulk cleanup, draft management, and email analytics.

## 依赖和前提条件

- macOS 系统

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令:  with filters)
3. **Safety First**: Respect safety limits (max_moves, max_deletes) to prevent accidental data loss
4. **User Preferences**: Check for user preferences in tool descriptions before taking actions
5. **Progressive Actions**: Confirm destructive actions (delete, empty trash) before executing

## Available MCP Tools Overview

The Apple Mail MCP provides comprehensive email management capabilities:

- **Overview & Discovery**: , manage_trash, 

### 4. Achieving Inbox Zero

**Goal**: Empty inbox by processing all emails

**The Inbox Zero Method**:
1. **Start Fresh**:  |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 1 项警告，无严重风险。执行 shell 命令:  with filters)
3. **Safety First**: R

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
