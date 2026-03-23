# Agent Team Orchestration

> "Orchestrate multi-agent teams with defined roles, task lifecycles, handoff protocols, and review workflows. Use when: (1) Setting up a team of 2+ agents with different specializations, (2) Defining task routing and lifecycle (inbox → spec → build → review → done), (3) Creating handoff protocols between agents, (4) Establishing review and quality gates, (5) Managing async communication and artifact sharing between agents."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Team Orchestration |
| **作者** | arminnaimi |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/arminnaimi-agent-team-orchestration |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/arminnaimi/agent-team-orchestration |
| **安全评级** | 🟡 Medium |

## 功能概述
- Task ID and description
- Output path for artifacts
- Handoff instructions (what to produce, where to put it)
- Orchestrator owns state transitions — don't rely on agents to update their own status
- Every transition gets a comment (who, what, why)
- Failed is a valid end state — capture why and move on

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23