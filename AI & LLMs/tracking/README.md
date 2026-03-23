# Gmgn Base Tracker

> Track tokens on Base chain via GMGN.AI. Covers Trenches (Almost Bonded & Migrated), Trending (1h), Discover (Smart Money, KOL, LIVE, Fresh Wallet, Sniper), and Monitor (Track Smart & KOL 1h). Use when users want to find trending tokens, discover new launches, follow smart money, or monitor KOL activity on Base chain.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Gmgn Base Tracker |
| **作者** | rzyen-hash |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/rzyen-hash-tracking |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rzyen-hash/tracking |
| **安全评级** | 🟡 Medium |

## 功能概述
- Always use web_search to fetch current, real-time data from GMGN.AI before responding.
- Present data in clean, structured tables with clear metrics.
- Always include clickable links to GMGN.AI and DexScreener for each token.
- Highlight standout signals (e.g. large smart money inflows, high sniper activity, near-bonding tokens).
- Add a brief analyst commentary after each table — what's notable, what to watch.
- Never fabricate token data. If search returns no results, say so and suggest the user check GMGN directly.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
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