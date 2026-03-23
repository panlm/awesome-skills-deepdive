# echodecks-ultimate

> EchoDecks 终极版 — 增强型 AI 卡片记忆学习系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | echodecks-ultimate |
| **作者** | drgeld |
| **ClawHub** | https://clawskills.sh/skills/drgeld-echodecks-ultimate |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/drgeld/echodecks-ultimate |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Turn your AI Agent into a Study Partner.
- Study with your Agent: "Quiz me on my Cardiology deck."
- Generate Content: "Create a deck about 'Machine Learning' and add 10 cards."
- Audio Learning: "Make a podcast conversation about this deck so I can listen while I drive."
- Flashcard Management: List decks, view cards.
- Spaced Repetition: Smart review system (Again, Hard, Good, Easy).

## 依赖和前提条件
- Study with your Agent:** "Quiz me on my Cardiology deck."
- Generate Content:** "Create a deck about 'Machine Learning' and add 10 cards."
- Audio Learning:** "Make a podcast conversation about this deck so I can listen while I drive."
- "What cards are due for review today?"*
- "Create a new deck called 'German Vocabulary'."*

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `echodecks_client.py` — 脚本文件
- `test_echodecks_client.py` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23