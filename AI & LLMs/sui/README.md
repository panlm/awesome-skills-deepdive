# Sui

> Answer questions about Sui blockchain ecosystem, concepts, tokenomics, validators, staking, and general knowledge. Use when users ask "what is Sui", "how does Sui work", "Sui vs other chains", or any Sui-related questions that aren't specifically about Move programming.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sui |
| **作者** | easonc13 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/easonc13-sui |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/easonc13/sui |
| **安全评级** | 🟡 Medium |

## 功能概述
- What is Sui? How does it work?
- Sui vs Ethereum/Solana/other chains
- SUI token, tokenomics, staking
- Validators, consensus, transactions
- Sui ecosystem, projects, wallets
- Object model, ownership concepts

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `setup.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23