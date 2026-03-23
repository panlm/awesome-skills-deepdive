# Stripe Best Practices

> 构建 Stripe 支付集成的最佳实践指南

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Stripe Best Practices |
| **作者** | ifoster01 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/ifoster01-stripe-best-practices |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ifoster01/stripe-best-practices |
| **安全评级** | 🟡 Medium |

## 功能概述
- Stripe 支付集成的最佳实践和规范
- 安全支付处理的实现指导
- 错误处理和重试策略
- PCI 合规性指南

## 使用场景
- 开发支付功能时参考 Stripe 最佳实践
- 审计现有 Stripe 集成的安全性和合规性

## 依赖和前提条件
- 无特殊依赖（知识型技能）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
