# Agent Autonomy Kit

> 让 AI Agent 不再等待指令，变成自主驱动、持续工作的独立员工

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Autonomy Kit |
| **作者** | ryancampbell |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/ryancampbell-agent-autonomy-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-autonomy-kit |
| **安全评级** | 🔴 High |

## 功能概述
- 任务队列系统：Agent 主动从持久化任务列表中拉取工作，而非被动等待
- 主动式 Heartbeat：将心跳检查从"有事吗？"转变为"做点有意义的事"
- 团队协调机制：Agent 间通过 Discord 等渠道进行进度更新和任务交接
- 令牌预算感知：智能管理每日令牌配额，合理分配到各项任务
- 任务发现能力：在工作过程中主动发现并添加新任务到队列
- 支持 GitHub Projects 作为任务管理后端

## 使用场景
- 让 Agent 在无人值守时持续推进项目任务，最大化订阅配额利用率
- 多 Agent 团队协作：自动分配、交接和汇报任务进展
- 构建 7x24 小时自主运行的 AI 工作流

## 依赖和前提条件
- Discord 或其他通信渠道（用于团队协调）
- 任务队列文件 tasks/QUEUE.md 或 GitHub Projects

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
