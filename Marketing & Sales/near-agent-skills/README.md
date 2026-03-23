# NEAR Agent Skills

> Comprehensive agentic skills for NEAR Protocol, including gas optimization and on-chain analytics.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | NEAR Agent Skills |
| **作者** | mastrophot |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/mastrophot-near-agent-skills |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mastrophot/near-agent-skills |
| **安全评级** | 🟢 Low |

## 功能概述
- `near_gas_estimate`: Estimate TGas for a transaction.
- `near_gas_optimize`: Get specific optimization tips for a contract.
- `near_gas_history`: View historical gas trends for an account.
- `near_gas_compare`: Compare NEAR costs to Ethereum (L1).
- `near_analytics_network`: Real-time network health and throughput.
- `near_analytics_whales`: Detection of high-value transactions.

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `molthub.json`
- `package-lock.json`
- `package.json`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23