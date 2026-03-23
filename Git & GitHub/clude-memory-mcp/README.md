# Clude Memory MCP

> 基于 Supabase + pgvector 的四层认知记忆系统 MCP 服务器——支持存储、回忆、搜索和"做梦"，具备类型特定衰减、赫布关联图谱和 Solana 链上提交。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Clude Memory MCP |
| **作者** | sebbsssss |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/sebbsssss-clude-memory-mcp |

## 功能概述
- `recall_memories`：基于相关性、重要性、近期性和向量相似度的多维记忆检索
- `store_memory`：存储跨对话持久化的记忆，支持四种类型——情景记忆、语义记忆、程序记忆和自我模型
- `get_memory_stats`：获取各类型记忆统计、平均重要性/衰减率、梦境会话历史和热门标签
- `get_market_mood`：获取当前市场情绪和价格状态（无 LLM 调用）
- `ask_clude`：向 Clude 提问并获取角色化回复
- 四层记忆架构：情景记忆（每日 7% 衰减）、语义记忆、程序记忆和自我模型，各有不同的衰减曲线

## 使用场景
- 为 AI Agent 构建跨对话的持久化认知记忆系统
- 实现基于赫布学习的记忆关联和自动强化
- 将重要记忆通过 Solana 进行链上不可变提交

## 依赖和前提条件
- Node.js（`npm install clude-bot`）
- 环境变量：`SUPABASE_URL`、`SUPABASE_SERVICE_KEY`
- Supabase 项目（需导入 `supabase-schema.sql` 数据库架构）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。供应链风险：需要安装外部依赖；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
