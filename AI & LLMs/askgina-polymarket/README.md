# Polymarket via Gina

> Fast setup for Claw bots: paste your Gina MCP token and start trading Polymarket in minutes.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Polymarket via Gina |
| **作者** | sidshekhar |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/sidshekhar-askgina-polymarket |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sidshekhar/askgina-polymarket |
| **安全评级** | 🟡 Medium |

## 功能概述
- Search: `"NBA markets tomorrow"`, `"Fed rate decision odds"`
- Trending: `"what's trending on Polymarket?"`, `"what are people betting on?"`
- Crypto / stocks: `"BTC 15 min up or down"`, `"AAPL daily market"`
- Trade: `"bet $10 on eagles to win"`, `"buy Yes at 0.40 or better"`
- Positions: `"show my positions"`, `"what's my P&L?"`
- Automate: `"daily market briefing at 9am"`, `"alert me on odds swings"`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23