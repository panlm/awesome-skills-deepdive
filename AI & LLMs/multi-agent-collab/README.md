# Multi-Agent Collaboration System Skills

> Universal multi-agent collaboration methodology for Claude Code. Model-tiered cowork + document-driven sync + self-evolution.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Multi-Agent Collaboration System Skills |
| **作者** | vdc-k |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/vdc-k-multi-agent-collab |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vdc-k/multi-agent-collab |
| **安全评级** | 🟢 Low |

## 功能概述
- Lead (High-capability model): Architecture, decisions, task breakdown
- Engineer (Balanced model): Execution, coding, implementation
- Maintainer (Cost-effective model): Archiving, cleanup, weekly reports
- `TASK.md` = Issue Board
- `CHANGELOG.md` = Commit Log (with #tags + agent identity)
- `CONTEXT.md` = Wiki (decision records + key insights)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `docs`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23