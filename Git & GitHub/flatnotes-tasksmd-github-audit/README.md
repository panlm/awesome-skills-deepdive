# Flatnotes + Tasks.md GitHub Audit

> "Thoroughly audit Tasks.md + Flatnotes for drift and accuracy; use GitHub (gh CLI) as source of truth to detect stale notes/cards and missing links. Produces a report and an optional fix plan."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Flatnotes + Tasks.md GitHub Audit |
| **作者** | branexp |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/branexp-flatnotes-tasksmd-github-audit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/branexp/flatnotes-tasksmd-github-audit |
| **安全评级** | 🟡 Medium |

## 功能概述
- Markdown report: `tmp/flatnotes-tasksmd-audit.md`
- JSON report: `tmp/flatnotes-tasksmd-audit.json`
- Tasks.md root: `/home/ds/.config/appdata/tasksmd/tasks`
- Flatnotes root: `/home/ds/.config/appdata/flatnotes/data`
- Flatnotes “system notes” mirror in workspace: `notes/resources/flatnotes-system/`
- `FLATNOTES_ROOT`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。凭证获取：需要 API 密钥或令牌；Prompt 注入：存在可疑 Prompt 模式；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23