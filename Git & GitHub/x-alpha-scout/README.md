# X Alpha Scout

> X/Twitter 加密货币和 NFT Alpha 情报扫描器，自动生成每日市场分析报告

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | X Alpha Scout |
| **作者** | hammadbtc |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/hammadbtc-x-alpha-scout |

## 功能概述
- 每日 UTC 00:00 自动生成综合 Alpha 报告（市场行情、新闻、CT 情绪、NFT 动态）
- 按需分析任意代币或 NFT 项目的 Crypto Twitter 情绪
- 覆盖 BTC、ETH、SOL 等主流加密货币市场动态
- 追踪 NFT 生态（ETH/BTC/SOL 链）的地板价和交易活跃度
- 汇总知名 KOL 和 Alpha 猎手的观点和预警
- 过滤噪音，提取结构化的可操作情报

## 使用场景
- 加密货币交易者获取每日 CT（Crypto Twitter）情报摘要
- 快速了解特定代币或 NFT 项目在 Twitter 上的讨论热度和社区情绪
- AI Agent 自动化加密市场监控和情报收集

## 依赖和前提条件
- `bird` CLI 工具（X/Twitter 命令行工具，通过 `brew install steipete/tap/bird` 安装）
- X/Twitter 认证凭证：`X_AUTH_TOKEN`（Auth Token）和 `X_CT0`（CT0 Cookie）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
