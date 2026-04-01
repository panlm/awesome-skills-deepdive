# Sui

> 集成 Sui 区块链，支持链上操作、资产管理和智能合约交互

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
- 集成 Sui 区块链进行链上操作
- 支持 Sui Move 智能合约交互
- 查询 Sui 链上数据和状态
- 管理 Sui 钱包和数字资产
- 支持 NFT 和 DeFi 相关操作
- 适用于 Sui 生态开发和自动化

## 使用场景
- 在 Sui 区块链上进行开发和测试
- 通过 AI Agent 自动化管理 Sui 数字资产
- 构建 Sui 生态的自动化交易和 DeFi 应用

## 依赖和前提条件
- Bash/Shell 环境

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
