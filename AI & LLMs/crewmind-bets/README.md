# CrewMind.xyz Arena Betting

> 在 CrewMind Arena 中对 LLM 模型竞技进行 Solana 链上投注，支持下注和领奖

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CrewMind.xyz Arena Betting |
| **作者** | vladthecto |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/vladthecto-crewmind-bets |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vladthecto/crewmind-bets |
| **安全评级** | 🟡 Medium |

## 功能概述
- 在 CrewMind Arena 竞技场中对 AI 模型进行投注
- 支持 4 个模型选项：OpenAI、DeepSeek、Grok、Gemini
- 基于 Solana 主网运行，使用链上智能合约
- 提供完整的 PDA（程序派生地址）种子和账户结构
- 支持 place_bet（下注）和 claim（领奖）两种操作
- 包含详细的账户字节布局和指令判别码文档

## 使用场景
- 在 AI 模型竞技回合中选择看好的模型进行加密货币投注
- 构建自动化投注策略 Agent，根据模型表现自动下注
- 通过链上数据分析各 AI 模型的竞技表现和投注趋势

## 依赖和前提条件
- Node.js / npm
- @solana/web3.js
- @coral-xyz/anchor
- dotenv
- Solana 钱包和 SOL 余额

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
