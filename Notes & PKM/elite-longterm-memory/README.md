# Elite Longterm Memory

> 精英长期记忆系统 — 高级持久化记忆与智能召回

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Elite Longterm Memory |
| **作者** | nextfrontierbuilds |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/nextfrontierbuilds-elite-longterm-memory |
| **安全评级** | 🔴 High |

## 功能概述
- 高级长期记忆持久化存储
- 基于语义的智能记忆召回
- 记忆重要性评分和优先级
- 自适应记忆容量管理
- 支持多模态记忆内容

## 使用场景
- AI Agent 长期记忆管理：跨会话存储和检索重要信息
- 对话中自动记录关键决策和信息供未来参考
- 多 Agent 协作中的知识共享和经验传递

## 依赖和前提条件
- Python 3.x
- Node.js 及相关依赖
- OpenAI API 密钥
- Anthropic API 密钥
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23