# letcairn.work

> Project management for AI agents using markdown files. Install and use the cairn CLI to create projects, manage tasks, track status, and coordinate human-AI collaboration through a shared workspace of markdown files.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | letcairn.work |
| **作者** | gregoryehill |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/gregoryehill-cairn-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gregoryehill/cairn-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- `AGENTS.md` — Compact reference for day-to-day operations (statuses, CLI commands, autonomy rules)
- `.cairn/planning.md` — Full guide for creating projects and tasks with real content
- path: ../artifacts/api-design-doc.md
- path: ../artifacts/test-plan.md
- `autonomy: execute` → `completed`
- `autonomy: draft` → `review` (requires approval)

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- Node.js / npm
- OAuth

## 包含文件
- `COMMANDS.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23