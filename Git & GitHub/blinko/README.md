# Blinko

> Play Blinko (on-chain Plinko) headlessly on Abstract chain. Use when an agent wants to play Blinko games, check game stats, view leaderboards, or track honey rewards. Handles the full commit-reveal flow including API auth, on-chain game creation, simulation, and settlement.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Blinko |
| **作者** | tolibear |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tolibear-blinko |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tolibear/blinko |
| **安全评级** | 🟡 Medium |

## 功能概述
- This skill signs on-chain transactions that spend real ETH. Use a dedicated hot wallet with only the funds you're willin
- Each game costs gas (Abstract chain) on top of your bet amount.
- Your private key is used locally to sign messages and transactions. It is sent to the Abstract RPC and Blinko API as sig
- Agents can invoke this skill autonomously when installed.
- 10 balls dropped through 8 rows of pins
- Bin multipliers: 2x, 1.5x, 0.5x, 0.2x, 0.1x, 0.1x, 0.2x, 0.5x, 1.5x, 2x

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23