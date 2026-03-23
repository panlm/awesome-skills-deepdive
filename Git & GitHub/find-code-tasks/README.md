# Find Code Tasks

> 列出仓库中所有代码任务及其状态、日期和元数据，快速了解待办工作或查找特定任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Find Code Tasks |
| **作者** | paulpete |
| **版本** | 1.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/paulpete-find-code-tasks |

## 功能概述
- 扫描仓库中所有 `.code-task.md` 文件，展示前置元数据中的状态和日期
- 支持按状态过滤：pending（待处理）、in_progress（进行中）、completed（已完成）、blocked（阻塞）
- 三种输出格式：表格（带状态符号）、JSON（程序化使用）、摘要（仅状态计数）
- 可自定义任务目录路径（默认 `.ralph/tasks/`）
- 解析任务 frontmatter（status、created、started、completed 字段）
- 与 code-task-generator 和 code-assist 等 Skill 集成

## 使用场景
- 开始工作前快速查看所有可用任务和积压情况
- 在执行代码辅助前后检查任务状态变化

## 依赖和前提条件
- Bash 环境（运行 task-status.sh 脚本）
- 仓库中存在 `.code-task.md` 格式的任务文件

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
