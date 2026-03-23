# Agent Team Kit

> *A framework for self-sustaining AI agent teams.*

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Team Kit |
| **作者** | ryancampbell |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/ryancampbell-agent-team-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-team-kit |
| **安全评级** | 🟡 Medium |

## 功能概述
- Work piles up waiting for one person to triage
- Nobody knows who owns what
- Great ideas get forgotten
- Nothing happens unless someone pushes
- `templates/process/INTAKE.md`
- `templates/process/ROLES.md`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `agents-config-draft.md`
- `package.json`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23