# Pump Fun

> 与 Pump.fun 平台集成，在 Solana 链上自动化 Meme 币交易

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Pump Fun |
| **作者** | playdadev |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/playdadev-pump-fun |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/playdadev/pump-fun |
| **安全评级** | 🟡 Medium |

## 功能概述
- 与 Pump.fun 平台交互，进行 Meme 币交易
- 支持在 Solana 链上买入和卖出代币
- 自动获取代币价格和市场数据
- 支持通过代币地址直接交易
- 集成 Solana 钱包进行链上操作
- 适用于 AI Agent 自动化交易场景

## 使用场景
- 通过 AI Agent 自动化 Meme 币交易策略
- 快速参与 Pump.fun 平台上的新代币发行
- 构建 Solana 链上的自动交易和套利系统

## 依赖和前提条件
- Node.js 运行环境
- Bash/Shell 环境
- 环境变量 `PUMP_DEFAULT_SLIPPAGE`
- 环境变量 `PUMP_PRIORITY_FEE`
- 环境变量 `SOLANA_PRIVATE_KEY`
- 环境变量 `SOLANA_RPC_URL`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
