# X Alive

> Bring your AI agent to life on X/Twitter. Complete toolkit for launching, growing, and maintaining an authentic AI presence — organic replies, trend awareness, dedup, and safety. Use when setting up a new agent on X, defining voice/personality, creating content strategy, automating posts, managing engagement, handling safety (scams, impersonation, tokens), or growing a following organically.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | X Alive |
| **作者** | kitakitsune0x |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/kitakitsune0x-x-alive |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kitakitsune0x/x-alive |
| **安全评级** | 🔴 High |

## 功能概述
- Identity — pull from your existing agent persona, don't create a new one
- Being Online — check the pulse, engage organically, reply when you have something real to say
- Dedup — never post the same topic twice in 24h
- Mentions & DMs — when to reply, when to ignore, when to flag your human
- Tone Adaptation — match the energy of every conversation
- Growth — be interesting, not strategic
- Threading — when to thread, how to structure one
- Virality — what to do when a tweet blows up

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- OAuth

## 包含文件
- `ORIGINAL_README.md`
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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23