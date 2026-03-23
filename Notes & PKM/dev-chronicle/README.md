# Dev Chronicle

> Generate narrative chronicles of developer work from git history, session transcripts, and memory files. Use when the user asks "what did I do today/this week", wants a work summary, daily/weekly chronicle, standup notes, or portfolio narrative. Also triggers on "chronicle", "dev diary", "work story", "recap", or "standup".

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Dev Chronicle |
| **作者** | sssamuelll |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/sssamuelll-dev-chronicle |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sssamuelll/dev-chronicle |
| **安全评级** | 🟢 Low |

## 功能概述
- "What did I do today?"
- "Generate a chronicle for this week"
- "Standup notes"
- "Write a portfolio narrative for [project]"
- Daily Chronicle — narrative recap with themes, decisions, and metrics
- Weekly Chronicle — arcs and progress over individual tasks

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Python / pip
- macOS

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `config.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23