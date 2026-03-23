# Agent Autonomy Kit

> Stop waiting for prompts. Keep working.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Autonomy Kit |
| **作者** | ryancampbell |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/ryancampbell-agent-autonomy-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-autonomy-kit |
| **安全评级** | 🔴 High |

## 功能概述
- Heartbeats check "anything need attention?" and reply `HEARTBEAT_OK`
- Team members sit idle until spawned
- Work stops when the human stops prompting
- Subscription limits (tokens/hour, tokens/day) go unused
- [ ] Research competitor X pricing
- [ ] Write blog post draft on memory systems

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23