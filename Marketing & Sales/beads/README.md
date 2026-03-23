# Beads Task Tracker

> Git-backed issue tracker for AI agents. Use when managing tasks, dependencies, or multi-step work. Triggers on task tracking, issue management, dependency graphs, ready work queues, or mentions of "beads" / "bd" CLI.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Beads Task Tracker |
| **作者** | rnijhara |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/rnijhara-beads |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rnijhara/beads |
| **安全评级** | 🟢 Low |

## 功能概述
- Always use `--json` for machine-readable output
- Never use `bd edit` — opens $EDITOR, unusable by agents
- Use `bd update` instead: `bd update <id> --title "New title" --description "New desc"`
- Run `bd sync` at end of session to flush changes to git

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。越权操作：涉及权限相关操作；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23