# Mnemon Memory

> "Persistent memory CLI for LLM agents. Store facts, recall past knowledge, link related memories, manage lifecycle."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mnemon Memory |
| **作者** | grivn |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/grivn-mnemon |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/grivn/mnemon |
| **安全评级** | 🟢 Low |

## 功能概述
- Skill → `~/.openclaw/skills/mnemon/SKILL.md`
- Hook → `~/.openclaw/hooks/mnemon-prime/` (agent:bootstrap — injects behavioral guide)
- Plugin → `~/.openclaw/extensions/mnemon/` (remind, nudge, compact hooks)
- Prompts → `~/.mnemon/prompt/` (guide.md, skill.md)
- Diff is built-in: duplicates skipped, conflicts auto-replaced.
- Output includes `action` (added/updated/skipped), `semantic_candidates`, `causal_candidates`.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- macOS
- Homebrew

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。命令执行：存在命令执行相关引用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23