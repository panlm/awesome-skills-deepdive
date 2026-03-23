# BoltzPay

> 自动化 API 数据付费工具，支持 x402 和 L402 双协议以及多链支付，实现无缝的数据交易

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BoltzPay |
| **作者** | leventilo |
| **版本** | 0.1.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/leventilo-boltzpay |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leventilo/boltzpay |
| **安全评级** | 🔴 High |

## 功能概述
- 支持 x402 和 L402 双协议自动付费
- 多区块链支付支持，灵活选择支付通道
- API 数据访问的自动化微支付
- 智能路由选择最优支付路径
- 交易记录和账单自动管理
- 无需人工干预的端到端付费流程

## 使用场景
- 智能体自动为付费 API 数据源支付访问费用
- 跨链支付场景下自动选择最低手续费通道
- 构建按量计费的数据服务交易系统

## 依赖和前提条件
- 配置加密货币钱包和支付通道
- 目标 API 支持 x402 或 L402 协议
- 网络环境支持区块链交易

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
