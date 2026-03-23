# Task Review Workflow

> 标准的 PR 审查与合并工作流，适用于任务驱动的开发模式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Task Review Workflow |
| **作者** | anikgnr |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/anikgnr-task-review-workflow |

## 功能概述
- 上下文收集：读取 PR 描述并查阅关联任务，确认预期行为和验收标准
- 基于 REVIEW_CHECKLIST.md 进行标准化审查：正确性、边界情况、回归、安全、性能、测试充分性
- 逐文件审查 Diff：标记逻辑缺陷、不安全假设、缺失验证、死代码和副作用风险
- 本地验证：拉取 PR 分支运行测试/lint/构建命令
- 清晰的审查反馈：区分必须修复项和可选建议
- 合并后自动执行：Trello 卡片移至 Done、删除任务分支（不删 main）
- 完成交接：向编程 Agent 发送最终结果（merged / CR sent / waiting for fixes）

## 使用场景
- AI 审查 Agent 按标准化流程审查编程 Agent 提交的 PR
- 需要将 PR 审查、Trello 任务管理和分支清理串联为自动化流程
- 多 Agent 协作开发中，确保审查完成后才开始下一个任务

## 依赖和前提条件
- Git 仓库
- REVIEW_CHECKLIST.md 审查基线文件
- Trello（或类似看板工具）

## 安全状态
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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive skill 自动生成
