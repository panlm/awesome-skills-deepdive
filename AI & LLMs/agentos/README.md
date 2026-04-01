# AgentOS SDK for Clawdbot

> 完整的 AgentOS SDK 集成，提供仪表盘同步、记忆持久化和项目管理功能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AgentOS SDK for Clawdbot |
| **作者** | agentossoftware |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/agentossoftware-agentos |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/agentossoftware/agentos |
| **安全评级** | 🟡 Medium |

## 功能概述
- 在心跳期间自动同步代理状态到 AgentOS Brain Dashboard
- 支持记忆持久化：上下文文件、每日笔记、项目分区、学习记录
- 提供 Golden Sync 同步模式，同时更新记忆和项目标签页
- 维护对话状态在 CONTEXT.md 中，确保会话连续性
- 支持项目管理：活动、任务、创意、变更日志、挑战
- 提供 CLI 工具 `aos` 进行快捷同步操作

## 使用场景
- 让用户通过 Brain Dashboard 实时监控 AI 代理的活动状态
- 跨会话保持代理的对话上下文和工作记忆
- 管理多项目的进度追踪和状态汇报

## 依赖和前提条件
- AgentOS 账号（brain.agentos.software）
- `agentos-golden-sync.sh` 或 `aos` CLI 工具
- OpenClaw / Clawdbot 环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
