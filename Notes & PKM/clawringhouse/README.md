# Clawringhouse - AI Shopping Concierge

> 信息交换中心 — Agent 间数据共享和协调

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Clawringhouse - AI Shopping Concierge |
| **作者** | francoisjosephlacroix |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/francoisjosephlacroix-clawringhouse |
| **安全评级** | 🟡 Medium |

## 功能概述
- 多 Agent 间数据共享和交换
- 信息路由和分发管理
- 跨会话数据协调
- 事件驱动的通信机制

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Python 3.x

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23