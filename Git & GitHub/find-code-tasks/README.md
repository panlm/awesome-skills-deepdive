# Find Code Tasks

> Lists all code tasks in the repository with their status, dates, and metadata. Useful for getting an overview of pending work or finding specific tasks.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Find Code Tasks |
| **作者** | paulpete |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/paulpete-find-code-tasks |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/paulpete/find-code-tasks |
| **安全评级** | 🟢 Low |

## 功能概述
- Starting a work session to see what tasks are available
- Checking status of tasks before/after running code-assist
- Finding tasks by status (pending, in_progress, completed)
- Getting a summary of task backlog
- Exporting task data for reporting
- filter (optional): Filter tasks by status

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `task-status.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。文件系统篡改：存在文件系统操作；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23