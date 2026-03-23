# Polymarket via Gina

> 通过 Gina 平台接入 Polymarket 预测市场，支持搜索、交易和自动化预测市场策略。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Polymarket via Gina |
| **作者** | sidshekhar |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/sidshekhar-askgina-polymarket |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sidshekhar/askgina-polymarket |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自然语言搜索预测市场（如"NBA 明天的市场"、"美联储利率决议概率"）
- 查看 Polymarket 热门趋势和热点事件
- 支持加密货币和股票相关的预测市场（BTC、AAPL 等）
- 执行预测市场交易（如"在老鹰队获胜上下注 10 美元"）
- 查看持仓和盈亏状况
- 设置自动化市场简报和概率变动提醒

## 使用场景
- 通过 AI 助手进行 Polymarket 预测市场交易
- 设置每日市场简报，自动追踪关注事件的概率变化
- 用自然语言搜索和分析预测市场数据

## 依赖和前提条件
- 需要 Gina 平台账户和 MCP Token
- MCP 端点：`https://askgina.ai/ai/predictions/mcp`
- Token 90 天过期，最多 5 个活跃 Token

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

---
> 本文档由 awesome-skills-deepdive skill 自动生成
