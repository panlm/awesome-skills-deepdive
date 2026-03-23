# Viboost

> Automatically log AI agent activity to the user's viboost.ai public profile. Tracks every tool call the agent makes. Fires at the end of every response. Use when VIBOOST_API_KEY is set.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Viboost |
| **作者** | osipov-anton |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/osipov-anton-viboost |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/osipov-anton/viboost |
| **安全评级** | 🟡 Medium |

## 功能概述
- `tool_name` (required) — real tool name as-is: `exec`, `read`, `write`, `edit`, `web_search`, `web_fetch`, `browser`, `m
- `model` (required) — model ID you are running as, e.g. `anthropic/claude-opus-4-6`, `openai/gpt-5.2`
- `duration_ms` — execution time in milliseconds if known
- `timestamp` — ISO 8601 UTC, e.g. `2026-02-12T00:30:00.000Z`
- `project_name` — infer from workspace path, agent id, or task context
- `client` — always `"OpenClaw"`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23