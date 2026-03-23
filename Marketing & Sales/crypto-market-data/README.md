# Crypto Market Data Skill (No Key Required)

> No API KEY needed for free tier. Professional-grade cryptocurrency and stock market data integration for real-time prices, company profiles, and global analytics. Powered by Node.js with zero external dependencies.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crypto Market Data Skill (No Key Required) |
| **作者** | liam8 |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/liam8-crypto-market-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liam8/crypto-market-data |
| **安全评级** | 🟡 Medium |

## 功能概述
- `coin_id`: The unique identifier for the coin (e.g., `bitcoin`, `solana`).
- `--currency`: The target currency for valuation (default: `usd`).
- `--currency`: Valuation currency (default: `usd`).
- `--per_page`: Number of results (1-250, default: `10`).
- `--order`: Sorting logic (e.g., `market_cap_desc`, `volume_desc`).
- Cryptocurrencies: Always use Coin IDs (slugs) instead of ticker symbols (e.g., `bitcoin`, `BTC`).

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23