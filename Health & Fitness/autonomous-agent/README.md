# Autonomous Agent Skills

> 自主代理任务执行框架

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
- Args: none
- Returns: `{ aptos: [{ address, network }], evm: [{ address, network }] }` — may be empty arrays
- When to use: Always call first before any wallet or paid tool action. Determines what exists
- Decision: If both arrays are empty → create wallets. If only one is empty → create the missing one. If both have entries → proceed to balance check or paid tools
- Args: `{ force?: boolean, network?: "testnet" | "mainnet" }` — defaults: force=false, network=testnet
- Returns: `{ success, address, network, message }` or `{ success: false, message, addresses }` if wallet exists and force=false
- When to use: When `get_wallet_addresses` returns empty `aptos` array, or user requests a new wallet
- Error handling: If `success: false` and wallet already exists, either use the existing wallet or retry with `force: true` to add another

## 使用场景
- 配置自主运行的 AI 代理任务
- 管理代理的目标和执行流程
- 监控自主代理的运行状态

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

## 安全状态
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
