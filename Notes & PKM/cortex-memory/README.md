# Cortex Memory

> 大脑皮层记忆系统 — 分层记忆存储与智能检索

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cortex Memory |
| **作者** | matthewubundi |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/matthewubundi-cortex-memory |
| **安全评级** | 🟢 Low |

## 功能概述
- 分层记忆架构（短期/长期/永久）
- 基于重要性的记忆强化和衰减
- 语义关联的智能检索
- 记忆容量自动管理和优化

## 使用场景
- AI Agent 长期记忆管理：跨会话存储和检索重要信息
- 对话中自动记录关键决策和信息供未来参考
- 多 Agent 协作中的知识共享和经验传递

## 依赖和前提条件
- Node.js
- Fabric 框架

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23