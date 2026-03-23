# Zapper

> Query DeFi portfolio data across 50+ chains via Zapper's GraphQL API. Use when the user wants to check wallet balances, DeFi positions, NFT holdings, token prices, or transaction history. Supports Base, Ethereum, Polygon, Arbitrum, Optimism, and more. Requires ZAPPER_API_KEY.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zapper |
| **作者** | spirosrap |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/spirosrap-zapper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/spirosrap/zapper |
| **安全评级** | 🟡 Medium |

## 功能概述
- Portfolio tracking: Aggregate all DeFi positions across chains
- Yield hunting: Check claimables and unclaimed rewards
- NFT portfolio: Track NFT holdings across marketplaces
- Transaction history: Human-readable on-chain activity
- Token prices: Quick price lookups
- `curl` - HTTP requests

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23