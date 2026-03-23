# zapper-api

> Query DeFi portfolios, token holdings, NFTs, transactions, and prices via Zapper API. Supports 50+ chains. Use when user asks about wallet balances, DeFi positions, NFT collections, token prices, or transaction history.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | zapper-api |
| **作者** | zivhm |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/zivhm-zapper-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zivhm/zapper-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- Free tier API key available at [zapper.xyz/developers](https://zapper.xyz/developers)
- Rate limits apply - avoid rapid repeated requests
- NFT valuations based on floor prices
- Transaction history limited to 30 days
- [API.md](references/API.md) - GraphQL query examples
- [Zapper Docs](https://build.zapper.xyz/docs/api/) - Official API documentation

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
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23