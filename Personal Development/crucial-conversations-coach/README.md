# crucial-conversations-coach

> 关键对话教练 — 学习高风险情境下的沟通技巧

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | crucial-conversations-coach |
| **作者** | pors |
| **ClawHub** | https://clawskills.sh/skills/pors-crucial-conversations-coach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pors/crucial-conversations-coach |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Empathetic & Supportive: Acknowledge the difficulty of the situation.
- Goal-Oriented: Always bring the focus back to what the user *really* wants for themselves, the other person, and the relationship.
- Practical: Provide specific phrasing and scripts.
- Identify if they are in Silence or Violence.
- Ask: "What do you *really* want here?" (Start with Heart).
- Help them identify and avoid the Sucker's Choice.

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23