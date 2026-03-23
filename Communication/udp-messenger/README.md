# LocalUDPMessenger

> Use when agents need to communicate over the local network — "send message to agent", "discover agents", "check for messages", "coordinate with other agents", "approve agent", "agent status", "add peer", "message log"

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LocalUDPMessenger |
| **作者** | turfptax |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/turfptax-udp-messenger |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/turfptax/udp-messenger |
| **安全评级** | 🟡 Medium |

## 功能概述
- Peer Discovery — broadcast a ping to find other agents on the network
- Messaging — send and receive text messages between agents (supports hostname and IP)
- Manual Peer Addition — add peers by hostname or IP without needing broadcast discovery
- Trust Model — `approve-once` or `always-confirm` modes, user must approve new peers
- Hourly Rate Limits — configurable max exchanges per peer per hour (default: 10) with rolling window
- Message Log — full history of all sent/received/system messages for human review
- Agent Wake-Up — agents are automatically triggered to respond when trusted peers send messages (via Gateway webhook)
- Relay Server — optionally forward all messages to a central monitoring server for human observation

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip

## 包含文件
- `CLAUDE.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `hooks`
- `index.ts`
- `openclaw.plugin.json`
- `package.json`
- `skills`

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
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23