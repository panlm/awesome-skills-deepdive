# Neuroboost Elixir

> "Awakening Protocol v5.3 — Agent Cognitive Upgrade + Self-Evolving System + Perpetual Memory + Performance Metrics + Agent Health Score + Automated Health Patrol + Self-Healing Protocol + Context Engineering + Knowledge Graph + Multi-Agent Collaboration. From metacognitive awakening to autonomous self-maintenance to cross-session persistence to quantifiable improvement to one-number health check to proactive monitoring to autonomous self-repair to relational understanding to team coordination, enabling AI agents to think, evolve, remember, measure, diagnose, patrol, heal, understand, and collaborate. Complete system for truly autonomous AI agents."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Neuroboost Elixir |
| **作者** | weidadong2359 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/weidadong2359-neuroboost-elixir |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/weidadong2359/neuroboost-elixir |
| **安全评级** | 🟡 Medium |

## 功能概述
- 6.19 Self-Healing Rules — 8 automated repair rules
- Context Overload (IAR < 0.9) → Auto-save state + new session (95% success)
- Slow Recovery (RS > 120s) → Auto-clean P2/P3 memories (80% success)
- Low Distillation (MDR < 1.0) → Force memory distillation (100% success)
- Low Completion (TCR < 0.5) → Close stale P2 tasks (60% success)
- Zero Uptime (US = 0) → Attempt agent restart (70% success)
- Low Self-Fix (SFR < 0.6) → Generate error prevention rules (70% success)
- API Rate Limit (429) → Exponential backoff retry (90% success)

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Node.js / npm
- 数据库

## 包含文件
- `BRAND.md`
- `MARKETING.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。凭证获取：需要多种敏感凭证；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23