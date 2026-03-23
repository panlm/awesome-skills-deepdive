# Crunch Protocol

> Natural language interface for Crunch Protocol CLI. Maps user requests to CLI commands for managing coordinators, competitions (crunches), rewards, and checkpoints. Supports output formatting for Slack, Telegram, Discord, or plain text.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crunch Protocol |
| **作者** | philippwassibauer |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/philippwassibauer-crunch-protocol |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/philippwassibauer/crunch-protocol |
| **安全评级** | 🟡 Medium |

## 功能概述
- Users can ask to add, update, or remove profiles. When they do, read the current `profiles.json`, apply the change, and 
- If `profiles.json` doesn't exist yet, create it with the structure above.
- When a user says _"set profile to m-jeremy"_ or _"use profile m-jeremy"_, remember it for the rest of the conversation a
- When a crunch name is provided, wrap it in quotes in the CLI command
- Common competition names: Crunch, Competition, Tournament, Challenge
- The action (get, create, start, end, list, etc.)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23