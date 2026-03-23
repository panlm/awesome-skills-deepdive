# feishu-memory-recall

> 飞书记忆召回 — 从飞书对话中提取和检索关键信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feishu-memory-recall |
| **作者** | autogame-17 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/autogame-17-feishu-memory-recall |
| **安全评级** | 🟡 Medium |

## 功能概述
- 从飞书对话中提取关键信息
- 飞书消息记忆索引和检索
- 跨群组信息关联
- 重要信息自动标记和归档

## 使用场景
- AI Agent 长期记忆管理：跨会话存储和检索重要信息
- 对话中自动记录关键决策和信息供未来参考
- 多 Agent 协作中的知识共享和经验传递

## 依赖和前提条件
- Node.js
- 飞书应用凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23