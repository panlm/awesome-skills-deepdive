# RHO Signals — Live Crypto TA Engine

> BTC、ETH、SOL、XRP 实时加密货币技术分析信号（RSI、MACD、EMA、布林带）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | RHO Signals — Live Crypto TA Engine |
| **作者** | jamierossouw |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jamierossouw-rho-signals |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jamierossouw/rho-signals |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时计算 RSI 相对强弱指标
- MACD 趋势跟踪和信号分析
- EMA 指数移动平均线计算
- 布林带通道分析和突破检测
- 支持 BTC、ETH、SOL、XRP 等主流币种
- 生成买入/卖出技术信号
- 多时间框架技术分析

## 使用场景
- 实时获取加密货币技术分析指标
- 基于技术信号辅助交易决策
- 监控加密货币市场趋势变化

## 依赖和前提条件
- 加密货币行情数据 API
- 配置监控币种和分析参数

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
