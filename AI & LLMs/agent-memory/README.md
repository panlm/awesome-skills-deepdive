# Agent Memory

> AI Agent 的持久化记忆系统——跨会话记住事实、从经验中学习、追踪实体

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Memory |
| **作者** | dennis-da-menace |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/dennis-da-menace-agent-memory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dennis-da-menace/agent-memory |
| **安全评级** | 🟢 Low |

## 功能概述
- 事实记忆：存储和召回跨会话的信息，支持标签、来源和置信度
- 经验学习：记录行动的成功或失败，提取可复用的洞察
- 实体追踪：跟踪人物、项目和偏好等实体信息
- 语义搜索：基于 FTS5 的快速相关记忆检索
- 自动清理：过期信息自动遗忘，保持记忆库精简
- 零外部依赖：仅需 Python + SQLite
- 支持记忆迭代更新（supersede）和历史记录保留

## 使用场景
- 让 Agent 记住用户偏好和历史交互，提供个性化服务
- 从过往失败经验中学习教训，避免重复犯错
- 跨多个会话追踪项目进展和关键人物信息

## 依赖和前提条件
- Python 3.8+
- SQLite（Python 标准库自带）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
