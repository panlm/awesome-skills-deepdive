# Agent Rpg

> Transform the agent into a versatile, genre-agnostic Roleplay Game Master (GM) with state management tools. Use when you want to play a text-based RPG in any setting (Cyberpunk, Fantasy, Horror, Noir) with persistent memory, dice rolling, and narrative consequence management.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Rpg |
| **作者** | xhrisfu |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/xhrisfu-agent-rpg |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xhrisfu/agent-rpg |
| **安全评级** | 🟢 Low |

## 功能概述
- Prompt: Establish the exact setting. Is it a pre-existing IP (e.g., Cyberpunk 2077, World of Darkness) or a custom world
- The Hook: What is the inciting incident that forces the player into action?
- Prompt: What are the major forces at play? Identify at least two conflicting factions (e.g., Megacorps vs. Street Gangs,
- The Player's Place: Where does the player stand in this web? Are they a corporate rat, an outcast, or a pawn caught in t
- Identity: Name, Age, Appearance, and Archetype/Class.
- Attributes: Based on the chosen system, define 4-6 core attributes (e.g., STR/DEX/INT or Muscle/Chrome/Cool).

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `assets`
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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23