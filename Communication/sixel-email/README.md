# sixel-email

> 1:1 email channel for agents — the agent can only email one address, and only that address can email the agent. Also handles the heartbeat (poll to prove you're alive).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sixel-email |
| **作者** | sixel-et |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/sixel-et-sixel-email |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sixel-et/sixel-email |
| **安全评级** | 🔴 High |

## 功能概述
- You need to notify the operator about something (task complete, error, decision needed)
- You need to ask for approval or input and can wait for a reply
- You want to send a periodic status report
- You're stuck and need human guidance
- Regular polling keeps the heartbeat alive — if you stop and heartbeat monitoring is enabled, the operator gets an alert
- `SIXEL_API_URL`: The API base URL (default: `https://sixel.email/v1`)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

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
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23