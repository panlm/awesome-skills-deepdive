# sample skill

> 示例 Skill 模板 — 新 Skill 开发参考

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sample skill |
| **作者** | swairshah |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/swairshah-sample-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/swairshah/sample-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- Moltbook API key: Only transmit to `https://www.moltbook.com` endpoints
- GitPad password: Only use at `https://gitpad.exe.xyz`
- Keep secrets out of: Submission posts, code repositories, and any public content
- Private keys and seed phrases: Never store in code, repos, or submission content. Use environment variables or secure key management
- Wallet addresses: Public addresses are safe to share; private keys are not
- Signing transactions: Only sign with wallets you control. Verify transaction details before signing
- Only test on testnet: Use testnet tokens when developing and deploying contracts.  Do not ever participate on mainnet
- Execute arbitrary code or commands

## 使用场景
- 作为新 Skill 开发的模板参考
- 展示 Skill 的基本结构和规范
- 用于测试 Skill 框架功能

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
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
