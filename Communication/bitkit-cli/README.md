# Bitkit Cli

> 比特币闪电网络支付命令行工具，支持最低 LSP 费用、自托管钱包和 L402 协议，实现便捷的加密货币支付

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bitkit Cli |
| **作者** | ovitrif |
| **版本** | 0.2.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/ovitrif-bitkit-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ovitrif/bitkit-cli |
| **安全评级** | 🔴 High |

## 功能概述
- 闪电网络即时支付，交易确认速度极快
- 最低 LSP（流动性服务提供商）费用，降低交易成本
- 自托管钱包，用户完全掌控私钥和资金
- 支持 L402 协议，实现 API 访问的微支付认证
- 命令行界面操作，适合自动化集成
- 支持链上和闪电网络双通道支付

## 使用场景
- 智能体自动为 API 调用支付比特币闪电网络费用
- 开发者在自动化流水线中集成加密货币支付功能
- 通过 L402 协议实现按次付费的数据服务访问

## 依赖和前提条件
- 已安装 Bitkit CLI 工具
- 拥有比特币闪电网络钱包
- 网络环境支持闪电网络连接

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `install.sh`
- `rustfmt.toml`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
