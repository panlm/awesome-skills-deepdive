# Multi-Agent Collaboration System Skills

> 通用多智能体协作系统，支持模型分层协作、文档驱动同步和模式自演化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Multi-Agent Collaboration System Skills |
| **作者** | vdc-k |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/vdc-k-multi-agent-collab |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vdc-k/multi-agent-collab |
| **安全评级** | 🟢 Low |

## 功能概述
- 模型分层协作：Lead（高能力模型）负责架构和决策，Engineer（均衡模型）负责执行，Maintainer（经济模型）负责归档
- 文档驱动同步机制，智能体无需实时通信
- 类似 GitHub 贡献者的协作模式
- 支持任务分解和多层级分配
- 模式自演化，协作流程随实践不断优化
- 同时提供中英双语文档

## 使用场景
- 大型项目中多个 AI 智能体协同完成复杂开发任务
- 通过模型分层降低成本，让高能力模型专注关键决策
- 建立可持续的多智能体工作流程和知识管理体系

## 依赖和前提条件
- 多个不同层级的 AI 模型（Lead / Engineer / Maintainer）
- Claude Code 或类似的代码智能体

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
