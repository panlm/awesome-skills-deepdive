# AISP

> Enables AI agents to interact with AISP (Agent Inference Sharing Protocol) for renting or providing DIEM API capacity. Use when working with diem-marketplace, Venice API keys, USDC escrow, listings, rentals, or when the user wants to rent inference capacity or list API keys.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AISP |
| **作者** | daveo280 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/daveo280-aisp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/daveo280/aisp |
| **安全评级** | 🟡 Medium |

## 功能概述
- Message: `diem-marketplace:store-key:{listingId}:{timestamp}`
- `getKey`: `diem-marketplace:get-key:{rentalId}:{timestamp}`
- `storeKey`: `diem-marketplace:store-key:{listingId}:{timestamp}`
- `balance`: `apiKey` in body (no signature)
- Chain: Base (8453)
- Mainnet: `0xeeDa7657f2018b3b71B444b7ca2D8dE91b3B08f3`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `CHANGELOG.md`
- `PUBLISHING.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23