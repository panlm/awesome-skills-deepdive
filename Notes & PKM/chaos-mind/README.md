# Chaos Mind

> Hybrid search memory system for AI agents. Manual search and storage - auto-capture is opt-in only.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Chaos Mind |
| **作者** | hargabyte |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/hargabyte-chaos-mind |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hargabyte/chaos-mind |
| **安全评级** | 🔴 High |

## 功能概述
- BM25 keyword matching (0.4 weight)
- Vector semantic search (0.4 weight)
- Graph relationships (0.1 weight)
- Heat/access patterns (0.1 weight)
- 43x faster than manual entry - captures context while you work
- Extracts decisions, insights, facts automatically with Qwen3-1.7B
- 100% local processing (no cloud/external APIs)
- Disabled by default for privacy - you control what it reads

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- macOS
- 数据库

## 包含文件
- `DEPLOYMENT_CHECKLIST.md`
- `INSTALL_NOTES.md`
- `ORIGINAL_README.md`
- `RELEASE_INSTRUCTIONS.md`
- `RELEASE_SUMMARY.md`
- `SECURITY.md`
- `SKILL.md`
- `_meta.json`
- `clawdhub.yaml`
- `config`
- `install.sh`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23