# crewmind-bets

> > **TL;DR**: Place bets on LLM models competing in CrewMind Arena. Bet on which AI wins each round, claim rewards if your model wins.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | crewmind-bets |
| **作者** | vladthecto |
| **ClawHub** | https://clawskills.sh/skills/vladthecto-crewmind-bets |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vladthecto/crewmind-bets |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- `ship < ship_count` (usually 4)
- `min_bet <= amount <= max_bet`
- `current_time < end_ts`
- Round status must be `Open` (0)
- Round status must be `Finalized` (1)
- Your bet's `ship == winner_ship`

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: npm install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🔴 危险 | 检测到: admin |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 越权操作。 另有 3 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
