# Context Anchor

> Recover from context compaction by scanning memory files and surfacing where you left off. Use when waking up fresh, after compaction, or when you feel lost about what you were doing.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Context Anchor |
| **作者** | boscoeuk |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/boscoeuk-context-anchor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/boscoeuk/context-anchor |
| **安全评级** | 🟢 Low |

## 功能概述
- Current task - What you were actively working on
- Active context - In-progress task files from `context/active/`
- Recent decisions - Key choices made in the last few days
- Open loops - TODOs, questions, and unfinished business
- [SKILL.md](./SKILL.md) - Full documentation
- [AGENTS.md](../../AGENTS.md) - Workspace conventions

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- macOS

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

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