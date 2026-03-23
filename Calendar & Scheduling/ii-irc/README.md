# ii-IRC

> Persistent IRC presence using ii (minimalist file-based IRC client) with event-driven mention detection. Use when setting up an AI agent on IRC, monitoring IRC channels, sending IRC messages, or integrating OpenClaw with IRC via ii. Covers ii setup, mention watcher, systemd services, and message sending/reading.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ii-IRC |
| **作者** | destructatron |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/destructatron-ii-irc |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/destructatron/ii-irc |
| **安全评级** | 🟡 Medium |

## 功能概述
- Not connecting: Check `ii` is running (`pgrep -f "ii -s"`), verify server/port
- Not joining channel: The `in` FIFO must exist; check `ExecStartPost` timing (increase sleep if needed)
- Mentions not triggering: Verify watcher is running (`pgrep -f watch-daemon`), check nick matches
- Messages splitting weirdly: Shorten messages; ii has a ~512 byte IRC protocol limit
- Reconnection: systemd `Restart=always` handles this; ii exits on disconnect, systemd restarts it

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，6 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23