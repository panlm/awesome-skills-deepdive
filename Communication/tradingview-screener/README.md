# TradingView Screener

> 基于 TradingView 数据筛选 6 大资产类别市场，API 预筛选结合 AI 智能分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TradingView Screener |
| **作者** | hiehoo |
| **版本** | 1.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/hiehoo-tradingview-screener |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hiehoo/tradingview-screener |
| **安全评级** | 🔴 High |

## 功能概述
- 覆盖股票、外汇、加密货币、期货、债券、指数 6 大类别
- 通过 TradingView API 进行多维度技术指标预筛选
- AI 分析筛选结果并生成投资洞察
- 支持自定义筛选条件和策略模板
- 实时数据驱动的市场扫描
- 生成结构化的筛选报告和排行榜

## 使用场景
- 交易者使用技术指标批量筛选符合策略的标的
- 每日盘前快速扫描市场发现交易机会
- 跨资产类别对比分析寻找最优配置

## 依赖和前提条件
- TradingView 账户（部分功能需 Pro）
- 基本的技术分析知识

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `assets`
- `install.sh`
- `references`
- `scripts`
- `state`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
