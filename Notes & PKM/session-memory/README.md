# Session Memory

> Persistent memory toolkit for AI agents. Save context, recall with relevance scoring, consolidate insights, track decisions across sessions. Features importance levels, multi-keyword search, session context loader, export/import, memory stats. Pure bash+node, no dependencies. v2.0.0

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Session Memory |
| **作者** | swaylq |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/swaylq-session-memory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/swaylq/session-memory |
| **安全评级** | 🟡 Medium |

## 功能概述
- Relevance-scored search — multi-keyword AND matching with importance + recency weighting
- Importance levels — low / normal / high / critical
- Session context loader — smart startup that loads recent + important memories
- Topic consolidation — group and review memories by topic
- Export / Import — backup and restore with deduplication
- Memory stats — totals, date range, avg/day, storage size, topic breakdown
- Edit / Delete — modify or remove entries by timestamp
- Pure bash + node — no npm dependencies

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23