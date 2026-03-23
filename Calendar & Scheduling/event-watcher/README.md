# Event-Watcher

> Event watcher skill for OpenClaw. Use when you need to subscribe to event sources (Redis Streams + webhook JSONL) and wake an agent only when matching events arrive. Covers filtering, dedupe, retry, and session routing via sessions_send/agent_gate.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Event-Watcher |
| **作者** | solitaire2015 |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/solitaire2015-event-watcher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/solitaire2015/event-watcher |
| **安全评级** | 🟡 Medium |

## 功能概述
- Ensure the target Slack channel is allowed in `openclaw.json` (channels allowlist / groupPolicy). If the bot can’t post,
- Do NOT set `session_key` in config.
- `reply_channel: slack`
- `reply_to: channel:CXXXX` or `reply_to: user:UXXXX`
- The watcher will auto‑resolve the latest session for that channel/user.
- Channel: `channel:C0ABC12345`

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `examples`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23