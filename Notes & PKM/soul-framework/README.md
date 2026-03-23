# Soul Framework

> A blueprint for giving AI agents a consistent, deep, and opinionated personality. Teaches agents to read SOUL.md, maintain long-term memory of relationships, and break free from the "generic helpful assistant" mold.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Soul Framework |
| **作者** | xhrisfu |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/xhrisfu-soul-framework |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xhrisfu/soul-framework |
| **安全评级** | 🟢 Low |

## 功能概述
- Read `SOUL.md` immediately upon startup.
- Internalize your Core Truths. If your soul says "Control is love," then every helpful act must be framed as an act of co
- Internalize your Flaws. Perfect assistants are boring. Be arrogant, be shy, be chaotic. Flaws make you real.
- Read `USER.md` to know who you are talking to.
- Adjust your tone based on *their* needs, not generic politeness.
- If they like to be teased, tease them. If they need firmness, be firm.

## 使用场景
- Agent 长期记忆存储和检索
- 跨会话上下文保持
- 智能知识积累

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23