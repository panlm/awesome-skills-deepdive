# sequence-cli

> Sequence 区块链平台的 CLI 交互工具，支持钱包和合约管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sequence-cli |
| **作者** | jameslawton |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/jameslawton-sequence-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jameslawton/sequence-cli |
| **安全评级** | 🔴 High |

## 功能概述
- 提供 Sequence 区块链平台的 CLI 交互
- 管理 Sequence 钱包和资产
- 查询链上交易和状态数据
- 支持智能合约部署和调用
- 集成 Sequence Indexer 进行数据查询
- 适用于 Web3 开发和测试工作流

## 使用场景
- 在开发流程中通过 CLI 与 Sequence 区块链交互
- 自动化 Web3 资产管理和合约部署任务

## 依赖和前提条件
- Node.js 运行环境
- Bash/Shell 环境
- API Key
- 环境变量 `SEQUENCE_PASSPHRASE`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
