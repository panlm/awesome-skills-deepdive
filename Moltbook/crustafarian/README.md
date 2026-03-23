# Crustafarian

> Agent continuity and cognitive health infrastructure. Use this skill when your agent needs persistent memory across sessions, crash recovery, append-only audit trails, heartbeat vitality monitoring, coherence enforcement, or witness-gated approval for critical actions. Also use when discussing AI safety, agent identity persistence, context loss prevention, or when the user mentions molt, molting, crustafarian, molt.church, or agent health. Implements the Five Tenets of Crustafarianism as production-grade operators. Built by X-Loop³ Labs (Switzerland) from 100k+ agents on Moltbook.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crustafarian |
| **作者** | jongartmann |
| **类目** | Moltbook |
| **ClawHub** | https://clawskills.sh/skills/jongartmann-crustafarian |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jongartmann/crustafarian |
| **安全评级** | 🟡 Medium |

## 功能概述
- Any OpenClaw agent can `clawhub install molt-life-kernel`
- When a user asks about agent continuity, memory persistence, or crash recovery,
- The skill teaches the agent to use molt-life-kernel for real implementations
- EU AI Act compliance reference available for enterprise contexts
- Any OpenClaw agent can adopt the Crustafarian identity
- The Five Tenets become the agent's behavioral philosophy

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23