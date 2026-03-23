# Collaboration Helper

> Track action items and coordination signals for the community, including quick task creation, status checks, and handoff notes. Use this when you need to log a collaborative task or check what everyone is currently working on.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Collaboration Helper |
| **作者** | crimsondevil333333 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/crimsondevil333333-collaboration-helper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/collaboration-helper |
| **安全评级** | 🟢 Low |

## 功能概述
- `list`: show every task, grouping by status.
- `add <title>`: create a new task with `--owner`, `--priority`, and `--note` fields.
- `complete <id>`: mark a task as done.
- GitHub: https://github.com/CrimsonDevil333333/collaboration-helper
- ClawHub: https://www.clawhub.ai/skills/collaboration-helper

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `data`
- `references`
- `scripts`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23