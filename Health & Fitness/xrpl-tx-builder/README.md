# XRPL Transaction Builder

> XRPL 交易构建工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | XRPL Transaction Builder |
| **作者** | harleyscodes |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/harleyscodes-xrpl-tx-builder |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/harleyscodes/xrpl-tx-builder |
| **安全评级** | 🟢 Low |

## 功能概述
- Drops: 1 XRP = 1,000,000 drops
- Address: Classic r-address (starts with 'r')
- Destination Tag: Optional memo for payments
- Flags: Transaction-specific options (see XRPL docs)

## 使用场景
- 构建和提交 XRP Ledger 交易
- 管理 XRPL 账户和密钥
- 查询 XRPL 链上数据和状态

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
