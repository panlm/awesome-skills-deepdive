# RHO Signals — Live Crypto TA Engine

> Real-time crypto TA signals for BTC, ETH, SOL, XRP. RSI, MACD, EMA, Bollinger Bands, OBV divergence, StochRSI — combined into a single directional score (-10 to +10) with Polymarket edge detection. Use when you need live crypto TA signals, directional bias, or Polymarket hourly market edge analysis.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | RHO Signals — Live Crypto TA Engine |
| **作者** | jamierossouw |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jamierossouw-rho-signals |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jamierossouw/rho-signals |
| **安全评级** | 🟢 Low |

## 功能概述
- Directional score (−10 to +10) per asset — negative = bearish, positive = bullish
- RSI with overbought/oversold detection
- OBV divergence — hidden accumulation/distribution signals
- Polymarket edge — compares TA-implied probability vs live market odds
- Counter-consensus alerts — when TA contradicts market >70% consensus

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
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23