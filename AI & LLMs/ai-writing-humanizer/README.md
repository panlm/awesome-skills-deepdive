# Ai Writing Humanizer

> Automatically strip AI writing patterns and stock phrases from user-facing prose before sending. Use when preparing longer texts to ensure a natural, human tone without obvious AI tells.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai Writing Humanizer |
| **作者** | hosthobbit |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/hosthobbit-ai-writing-humanizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hosthobbit/ai-writing-humanizer |
| **安全评级** | 🟢 Low |

## 功能概述
- Overuse of hedging phrases: "At the end of the day", "It's worth noting", "It is important to remember"
- Stock transitions and signposts: "First", "Secondly", "Finally"
- Structural markers: em dashes (—), parentheses for side notes, bullet-like serial lists
- Predictable rule-of-three constructs: "X, Y, and Z" used as checklist language
- Passive voice sections flagged by "was", "were", "has been"
- Performed authenticity cues: "I hope this helps", "Let me know if you have any questions"

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `tests`

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