# Elite Longterm Memory

> "Ultimate AI agent memory system for Cursor, Claude, ChatGPT & Copilot. WAL protocol + vector search + git-notes + cloud backup. Never lose context again. Vibe-coding ready."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Elite Longterm Memory |
| **作者** | nextfrontierbuilds |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/nextfrontierbuilds-elite-longterm-memory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/elite-longterm-memory |
| **安全评级** | 🔴 High |

## 功能概述
- ✅ Bulletproof WAL Protocol — Write-ahead logging survives compaction
- ✅ LanceDB Vector Search — Semantic recall of relevant memories
- ✅ Git-Notes Knowledge Graph — Structured decisions, branch-aware
- ✅ File-Based Archives — Human-readable MEMORY.md + daily logs
- ✅ Cloud Backup — Optional SuperMemory sync
- ✅ Memory Hygiene — Keep vectors lean, prevent token waste

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `package.json`

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