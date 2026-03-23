# Pump Fun

> Buy, sell, and launch tokens on Pump.fun using the PumpPortal API

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Pump Fun |
| **作者** | playdadev |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/playdadev-pump-fun |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/playdadev/pump-fun |
| **安全评级** | 🟡 Medium |

## 功能概述
- `/pump-buy 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 0.1` - Buy 0.1 SOL worth of tokens
- `/pump-buy 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 0.5 15` - Buy with 15% slippage
- `/pump-sell 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 1000000` - Sell 1,000,000 tokens
- `/pump-sell 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 100%` - Sell all tokens
- `/pump-sell 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU 50% 10` - Sell 50% with 10% slippage
- `/pump-launch "My Token" MTK "A revolutionary token" 1` - Launch with 1 SOL dev buy

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23