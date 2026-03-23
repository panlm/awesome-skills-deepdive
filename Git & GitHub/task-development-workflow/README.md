# Task Development Workflow

> TDD 优先的结构化开发工作流，包含需求澄清、计划审批、任务跟踪和 PR 代码审查

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Task Development Workflow |
| **作者** | anikgnr |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/anikgnr-task-development-workflow |

## 功能概述
- 需求澄清阶段：在实现前强制进行业务需求、UI/UX、架构决策等方面的问题澄清
- 计划审批门控：提交详细任务分解计划，需获得明确批准后才能开始实现
- Trello 看板集成：使用 Backlog → To Do → In Progress → Review → Done 流程管理任务
- TDD 强制执行：先写测试 → 运行失败 → 实现功能 → 测试通过（除非获得明确豁免）
- 分支策略：禁止直接推送到 main，每个任务创建独立功能分支
- PR 反馈循环：PR 包含 Trello 链接，CR 评论触发返工直至通过
- 串行合并门控：当前 PR 合并后才能开始下一个任务

## 使用场景
- AI 编程 Agent 执行软件开发任务时，需要遵循结构化的质量保证流程
- 团队需要强制执行 TDD、代码审查和计划审批的标准化开发工作流
- 需要将需求澄清、任务跟踪、Git 分支策略和 PR 审查串联为完整流程

## 依赖和前提条件
- Git 仓库
- Trello（或类似看板工具）用于任务跟踪
- 代码审查人（Reviewer）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive skill 自动生成
