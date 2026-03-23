# BrainDB

> Persistent, semantic memory for AI agents. Gives your AI long-term recall that survives compaction and session resets — 98% accuracy, 20ms latency.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BrainDB |
| **作者** | chair4ce |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/chair4ce-braindb |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chair4ce/braindb |
| **安全评级** | 🔴 High |

## 功能概述
- Semantic search — 768-dimensional embeddings via all-mpnet-base-v2. Finds conceptually related memories, not just keywor
- Four memory types — Episodic (events), semantic (facts), procedural (skills), and association (links between memories).
- Tiered ranking — Semantic similarity always outranks keyword matches. No more irrelevant results beating relevant ones.
- Auto-deduplication — Won't store near-duplicate memories (configurable threshold, default 0.90).
- Hebbian reinforcement — Memories strengthen with use, decay without it. Important memories persist; noise fades.
- Motivation-weighted encoding — Encoding strength varies by emotional/motivational context.
- Query expansion — Understands colloquial phrases ("how do we make money" → revenue, profit, pricing).
- 43ms average recall at 1,000 memories. Scales to 10K+.

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- Docker
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `auto-capture.js`
- `config.json`
- `docker-compose.yml`
- `embedder.py`
- `execution-awareness.js`
- `gateway.js`
- `install.sh`
- `migrate.cjs`
- `package.json`
- `setup.sh`
- `uninstall.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23