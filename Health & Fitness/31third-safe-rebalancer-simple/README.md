# 31Third Safe Rebalancer (Simple)

> One-step Safe rebalancer using on-chain 31Third policies.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | 31Third Safe Rebalancer (Simple) |
| **作者** | phips0812 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/phips0812-31third-safe-rebalancer-simple |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/phips0812/31third-safe-rebalancer-simple |
| **安全评级** | 🟡 Medium |

## 功能概述
- Fails if executor wallet is not equal to `ExecutorModule.executor`.
- Fails if required policies are missing.
- Loads `driftThresholdBps` from StaticAllocation and skips execution when drift is below threshold.
- Uses `StaticAllocation.priceOracle` / `Slippage.priceOracle` for pricing.
- Loads `maxSlippageBps` from SlippagePolicy and uses:
- `maxSlippage = policySlippage - 0.1%`
- `maxPriceImpact = policySlippage - 0.1%`
- Uses default `minTradeValue = 0.1`.

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `abi`
- `dist`
- `index.ts`
- `package-lock.json`
- `package.json`
- `scripts`
- `skill.json`
- `skill.yaml`
- `src`
- `tests`
- `tsconfig.json`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23