# Agent-manager-for-AI-planner

> AI 规划器的智能体管理工具，用于创建、监控和调度子智能体

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent-manager-for-AI-planner |
| **作者** | nonightwatch |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/nonightwatch-agentmanager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nonightwatch/agentmanager |
| **安全评级** | 🔴 High |

## 功能概述
- 创建和销毁子智能体实例
- 监控智能体运行状态和健康度
- 任务分配和执行进度追踪
- 智能体间通信协调
- 资源使用管理和限制

## 使用场景
- AI 规划器需要动态管理多个执行智能体
- 复杂任务分解后分发给多个子智能体执行
- 监控和协调智能体集群的运行

## 依赖和前提条件
- 支持多智能体的运行环境
- 规划器与管理器的集成配置

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `_meta.json`
- `openapi`
- `package-lock.json`
- `package.json`
- `skill.md`
- `src`
- `tests`
- `tsconfig.json`
- `vitest.config.ts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
