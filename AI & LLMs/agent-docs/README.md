# Agent Docs

> Create documentation optimized for AI agent consumption. Use when writing SKILL.md files, README files, API docs, or any documentation that will be read by LLMs in context windows. Helps structure content for RAG retrieval, token efficiency, and the Hybrid Context Hierarchy.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Docs |
| **作者** | tylervovan |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/tylervovan-agent-docs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tylervovan/agent-docs |
| **安全评级** | 🟡 Medium |

## 功能概述
- NO SECRETS in output
- Use `app/` directory ONLY
- Auth: `docs/auth/llms.txt`
- DB: `docs/db/schema.md`
- Security rules, architecture constraints
- Build/test/lint commands (top for primacy bias)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23