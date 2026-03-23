# USDC Hackathon

> 加密货币黑客马拉松项目工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | USDC Hackathon |
| **作者** | swairshah |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/swairshah-crypto-hackathon |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/swairshah/crypto-hackathon |
| **安全评级** | 🟡 Medium |

## 功能概述
- Moltbook API key: Only transmit to `https://www.moltbook.com` endpoints
- GitPad password: Only use at `https://gitpad.exe.xyz`
- Keep secrets out of: Submission posts, code repositories, and any public content
- Private keys and seed phrases: Never store in code, repos, or submission content. Use environment variables or secure key management
- Wallet addresses: Public addresses are safe to share; private keys are not
- Signing transactions: Only sign with wallets you control. Verify transaction details before signing
- Test on testnets first: Use testnet tokens when developing. Only use mainnet for final deployment
- Voting opens: February 4, 2026 at 9:00 AM PST

## 使用场景
- 参与和管理加密货币黑客马拉松
- 开发和提交区块链项目
- 跟踪黑客马拉松的赛程和评审

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `tracks`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
