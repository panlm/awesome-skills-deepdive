# Craft Notes

> Manage Craft notes, documents, and tasks via CLI. Use when the user asks to add notes, create documents, manage tasks, search their Craft documents, or work with daily notes. Craft is a note-taking app for macOS/iOS.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Craft Notes |
| **作者** | noah-ribaudo |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/noah-ribaudo-craft |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/noah-ribaudo/craft |
| **安全评级** | 🟢 Low |

## 功能概述
- Markdown content passed as arguments; escape quotes if needed
- Dates: `today`, `yesterday`, or `YYYY-MM-DD`
- Task scopes: `inbox` (default), `active`, `upcoming`, `logbook`
- Document locations: `unsorted`, `trash`, `templates`, `daily_notes`

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- macOS

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23