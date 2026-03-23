# LI.FI Orchestrator

> Cross-chain bridging and swapping via LI.FI — the leading bridge aggregator that routes across 30+ bridges and DEXs for optimal rates. Use when you need to: (1) Get quotes for moving tokens between chains, (2) Execute cross-chain swaps with best pricing, (3) Track bridge transaction status, (4) Compare routes across protocols like Stargate, Across, Hop, Celer, etc. Supports Ethereum, Polygon, Arbitrum, Optimism, Base, BSC, Avalanche, Solana, and 15+ other chains. Handles native tokens and ERC-20s with automatic slippage protection.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LI.FI Orchestrator |
| **作者** | rhlsthrm |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/rhlsthrm-lifi-orchestrator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rhlsthrm/lifi-orchestrator |
| **安全评级** | 🟡 Medium |

## 功能概述
- Endpoint: `https://li.quest/v1`
- Auth: Optional API key via `x-lifi-api-key` header (higher rate limits)
- Rate limit: 10 req/min without key, higher with key
- USDC (Ethereum): `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`
- USDC (Polygon): `0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359`
- USDT (Ethereum): `0xdAC17F958D2ee523a2206206994597C13D831ec7`

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

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