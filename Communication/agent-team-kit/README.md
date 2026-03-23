# Agent Team Kit

> 自维持 AI 智能体团队框架，支持多智能体协作和团队自主运作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Team Kit |
| **作者** | ryancampbell |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/ryancampbell-agent-team-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-team-kit |
| **安全评级** | 🔴 High |

## 功能概述
- 创建和管理多智能体协作团队
- 团队内任务自动分配和调度
- 智能体间角色分工和职责定义
- 团队运行状态监控和自我修复
- 支持团队成员动态增减

## 使用场景
- 搭建多智能体协同工作团队处理复杂项目
- 构建自运行的智能体服务团队
- 需要多角色分工配合的自动化任务

## 依赖和前提条件
- OpenClaw 环境支持多智能体运行
- 团队配置文件定义角色和任务流

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `agents-config-draft.md`
- `package.json`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
