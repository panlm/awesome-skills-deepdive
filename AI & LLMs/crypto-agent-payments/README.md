# Crypto Wallets & Payments for AI Agents

> 为 AI Agent 提供加密货币钱包创建、代币转账和跨链兑换功能，支持自动化支付

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crypto Wallets & Payments for AI Agents |
| **作者** | nicofains1 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/nicofains1-crypto-agent-payments |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nicofains1/crypto-agent-payments |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建 ERC20 兼容钱包并安全存储密钥
- 支持发送 ETH、USDC 及任意 ERC20 代币到任意地址
- 跨 13 条链提供最优汇率的代币兑换服务
- 支持推荐人费用机制，推荐人可获得 80% 的额外手续费
- 通过 MCP Server 集成 OnlySwaps 服务
- 提供只读工具（获取报价、查看组合）和钱包操作工具

## 使用场景
- Agent 自动执行 Bug 赏金发放和奖励支付
- 构建 Agent 间的自动化加密货币交易和结算系统
- 为 AI 服务创建自动化的跨链代币兑换和收款流程

## 依赖和前提条件
- Node.js / npm
- @onlyswaps/mcp-server（通过 npx 运行）
- PRIVATE_KEY 环境变量（钱包操作需要）
- mcporter（OpenClaw MCP 配置）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
