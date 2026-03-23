# Rune - Self-Improving AI Memory

> Self-improving AI memory system with intelligent context injection and adaptive learning

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Rune - Self-Improving AI Memory |
| **作者** | thebobloblaw |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/thebobloblaw-rune |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/thebobloblaw/rune |
| **安全评级** | 🔴 High |

## 功能概述
- Fact Storage — Structured key-value facts with categories, confidence scores, scopes, and tiers
- Full-Text Search — FTS5-powered instant search across all facts
- Auto-Extraction — Extract facts from markdown session files using Ollama, Anthropic, or OpenAI
- Adaptive Context — Dynamically inject relevant facts into LLM prompts with token budgets
- Session Intelligence — Detect interaction styles, analyze patterns, proactive recall
- Project Autopilot — Track project states, suggest next tasks, detect stuck projects
- Smart Notifications — Classify, batch, and queue notifications for optimal timing
- Self-Improvement — Weekly self-review, pattern analysis, skill usage tracking

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `CHANGELOG.md`
- `COMMON-MISTAKES.md`
- `INTEGRATION-GUIDE.md`
- `ORIGINAL_README.md`
- `SECURITY.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `install.sh`
- `package.json`
- `rune-session-handler.sh`
- `setup-workflow.sh`
- `skill.json`
- `src`
- `uninstall.sh`
- `update.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23