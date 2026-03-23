# Autonomous Agent Skills

> CornerStone MCP x402 skill for agents. Tools for stock predictions, backtests, bank linking, and agent/borrower scores. Payment-protected MCP tools (run_prediction, run_backtest, link_bank_account, get_agent_reputation_score, get_borrower_score, by-email variants) with x402 flow (Aptos + Base). Skill handles 402 → pay → retry. Wallet attestation for onboarding. For marketplaces where agents download and use skills autonomously.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Autonomous Agent Skills |
| **作者** | josephrp |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/josephrp-autonomous-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/josephrp/autonomous-agent |
| **安全评级** | 🔴 High |

## 功能概述
- Runtime: Node.js 18+
- Runner: LangChain.js (ReAct), OpenAI-compatible LLM (e.g. Hugging Face) for the demo; agents use the tools via their own
- MCP: [Model Context Protocol](https://modelcontextprotocol.io) + x402 payment flow
- Chains: Aptos (viem-style + @aptos-labs/ts-sdk), EVM (viem) for Base Sepolia/Base
- Payments: x402 facilitator (verify/settle), local wallet storage
- Wallets: Stored locally (e.g. `~/.aptos-agent-wallets.json`, `~/.evm-wallets.json`) for the agent using the skill; priva

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `LICENSE.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `adapters`
- `package-lock.json`
- `package.json`
- `skills`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23