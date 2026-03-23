# agents-manager

> Clawdbot 多代理管理器：发现、注册、分层路由和任务分配

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agents-manager |
| **作者** | agentandbot-design |
| **ClawHub** | https://clawskills.sh/skills/agentandbot-design-agents-manager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/agentandbot-design/agents-manager |
| **安全评级** | 🟢 Low |

## 功能概述
- 中央注册表管理所有代理
- 严格的层级结构（reports_to/can_assign_to）
- 握手协议实现安全任务委派
- 代理能力卡片标准化
- Mermaid 可视化代理层级图
- 健康检查和性能统计
- 交互式设置向导

## 使用场景
- 管理多个 Clawdbot 代理的协作
- 定义代理间的任务路由和权限
- 监控代理健康状态和性能

## 依赖和前提条件
Node.js

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references/agent-profile-schema.md`
- `references/agent-registry.md`
- `references/health-check-template.md`
- `references/task-routing-rules.md`
- `scripts/can_assign.js`
- `scripts/generate_card.js`
- `scripts/health_check.js`
- `scripts/log_analyzer.js`
- `scripts/scan_agents.js`
- `scripts/setup_wizard.js`
- `scripts/validate_registry.js`
- `scripts/visualize_agents.js`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 8 个 JS 脚本通过 node 执行，读写本地文件 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Node.js 标准库 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 agent-registry.md 注册表文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 权限检查逻辑中 main 角色有超级权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化守护进程 |
| SEC-09 信息采集 | 🟢 Safe | 仅读取本地注册表数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，逻辑简单 |

**综合评级: 🟢 Low**
**风险摘要:** 本地文件操作为主的管理工具，脚本逻辑简单透明

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
