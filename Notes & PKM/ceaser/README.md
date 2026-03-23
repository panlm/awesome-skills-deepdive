# Openclaw Skill

> Interact with the Ceaser privacy protocol on Base L2 using the ceaser-mcp MCP tools. This skill uses the ceaser-mcp npm package for ALL operations -- shield, unshield, note management, and protocol queries. All ceaser tool calls use CLI subcommands (npx -y ceaser-mcp <subcommand>). Ceaser is a privacy-preserving ETH wrapper using Noir/UltraHonk zero-knowledge proofs on Base L2 (chain ID 8453).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Openclaw Skill |
| **作者** | zyra-v21 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/zyra-v21-ceaser |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zyra-v21/ceaser |
| **安全评级** | 🔴 High |

## 功能概述
- Check denominations and fees before shielding
- Monitor pool TVL and note count
- Verify a nullifier is unspent before attempting unshield
- Check facilitator health and circuit breaker state
- Browse indexed commitments and Merkle tree state

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23