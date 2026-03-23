# mt5_trade

> 通过本地 MT5 交易 HTTP API 执行交易操作，采用信号→草案→确认的安全三步流程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mt5_trade |
| **作者** | xuanyushen19 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/xuanyushen19-mt5trade |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xuanyushen19/mt5trade |
| **安全评级** | 🔴 High |

## 功能概述
- 对接本地 MetaTrader 5 交易 HTTP API
- 信号→草案→确认的三步安全交易流程
- 交易指令需人工确认后才执行
- 支持外汇、期货、股票等多品种交易
- 实时行情数据查询
- 持仓和订单状态管理
- 交易风险控制和止损设置

## 使用场景
- AI 分析行情信号后生成交易草案供人工确认
- 自动化交易策略的安全执行（带人工审批）
- 实时监控持仓并在触发条件时提醒操作

## 依赖和前提条件
- 本地运行的 MetaTrader 5 终端
- MT5 交易 HTTP API 服务已启动
- 有效的交易账户和资金
- API 端口和认证配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
