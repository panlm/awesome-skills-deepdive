# Stripe Agent Wallet | Use Stripe top-up your agentic wallet - Private Beta

> 使用 CreditClaw + Stripe 在任何地方进行在线支付

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Stripe Agent Wallet | Use Stripe top-up your agentic wallet - Private Beta |
| **作者** | jononovo |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/jononovo-stripe |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jononovo/stripe |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 Stripe 处理在线支付
- 管理支付方式和客户信息
- 查看交易记录和支付状态
- 支持订阅和一次性支付

## 使用场景
- Agent 使用 Stripe 在网站上完成支付
- 管理 Stripe 账户的支付方式和交易历史

## 依赖和前提条件
- API Key（Stripe）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
