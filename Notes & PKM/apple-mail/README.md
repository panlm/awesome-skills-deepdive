# Apple Mail

> Apple Mail.app integration for macOS. Read inbox, search emails, send emails, reply, and manage messages with fast direct access (no enumeration).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apple Mail |
| **作者** | tyler6204 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/tyler6204-apple-mail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-mail |
| **安全评级** | 🟢 Low |

## 功能概述
- Script monitors database message count
- Returns early when sync completes (no changes for 2s)
- Reports new message count: `Sync complete in 2s (+3 messages)`
- Mail.app must be running (script will error if not)
- `mail-list.sh` does NOT auto-refresh — call `mail-refresh.sh` first if you need fresh data
- `●` = unread, blank = read

## 使用场景
- 管理和处理邮件
- 自动邮件分类和回复
- 邮件内容提取和分析

## 依赖和前提条件
- macOS
- 数据库

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
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23