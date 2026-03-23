# Macro Regime Detector

> Detect the current macro regime (Risk-On, Risk-Off, Inflationary, Deflationary, Stagflation) using multi-source intelligence. Combines Fear & Greed, DXY, yield curve, VIX, gold/BTC ratio, Reddit sentiment, and major news events. Use when you need macro regime analysis, risk-on vs risk-off determination, portfolio positioning advice, or crypto market context.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Macro Regime Detector |
| **作者** | jamierossouw |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/jamierossouw-macro-regime-detector |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jamierossouw/macro-regime-detector |
| **安全评级** | 🟢 Low |

## 功能概述
- Fear & Greed (`alternative.me/fng`): 0-100 score, regime anchor
- Reddit pulse: r/CryptoCurrency, r/investing hot posts, bearish/bullish ratio
- DXY proxy: BTC/USD inverse correlation check
- News NLP: major economic event detection (Fed, CPI, NFP, SEC)
- On-chain: BTC exchange flows, miner capitulation signals
- Feb 21 2026: Regime B (Neutral/Cooling) | F&G=8, "Extreme Fear" | Contrarian bullish signal active

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 包含文件
- `SKILL.md`
- `_meta.json`

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