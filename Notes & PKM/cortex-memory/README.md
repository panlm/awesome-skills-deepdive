# Cortex Memory

> Long-term memory for OpenClaw agents — auto-recall before turns, auto-capture after, tools for search/save/forget.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cortex Memory |
| **作者** | matthewubundi |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/matthewubundi-cortex-memory |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matthewubundi/cortex-memory |
| **安全评级** | 🟢 Low |

## 功能概述
- Key patterns, schemas, or formats (e.g. `arclight:user:{userId}`, cache-aside strategy)
- Exact metrics and performance numbers (before/after)
- SQL statements, CLI commands, config values
- Library/package choices with version-specific rationale (e.g. "chose SendGrid over Resend because SOC 2 Type 2")
- Architecture/migration decisions with specific reasoning
- Bug root causes with the full debugging chain

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23