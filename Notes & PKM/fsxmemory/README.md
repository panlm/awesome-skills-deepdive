# ForesigxtMemory

> Structured memory system for AI agents. Context death resilience (checkpoint/recover), structured storage, Obsidian-compatible markdown, and local semantic search.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ForesigxtMemory |
| **作者** | azrijamil |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/azrijamil-fsxmemory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/azrijamil/fsxmemory |
| **安全评级** | 🔴 High |

## 功能概述
- YAML frontmatter with metadata (title, date, type, status)
- Structured sections with placeholder guidance
- Wiki-link suggestions for connections
- Auto-generated tags
- ✅ Isolating workspace memory — Each project has its own separate vault
- ✅ Per-project configuration — Different agents in different workspaces use different vaults

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `INSTALL.md`
- `SKILL.md`
- `_meta.json`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，4 项中风险。数据外泄：大量外部数据传输；文件系统篡改：涉及危险文件操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23