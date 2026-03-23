# Agent-manager-for-AI-planner

> Agent Manager is a Node.js + TypeScript + Express orchestration service for external AI clients.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent-manager-for-AI-planner |
| **作者** | nonightwatch |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/nonightwatch-agentmanager |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nonightwatch/agentmanager |
| **安全评级** | 🟡 Medium |

## 功能概述
- Dynamic planning over HTTP with pluggable planner strategies.
- Asynchronous `/v1/run` execution with `run_id` polling and `/v1/run/:id/events` incremental feeds.
- Optional client-supplied plan execution (`POST /v1/run` with `plan`).
- Cost-aware execution with model tiers, owner pricing caps, retries, upgrades, and fallback.
- Tool hardening for public usage:
- registration disabled by default

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `_meta.json`
- `openapi`
- `package-lock.json`
- `package.json`
- `skill.md`
- `src`
- `tests`
- `tsconfig.json`
- `vitest.config.ts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23