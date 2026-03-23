# yumstock

> YumStock 美食和库存管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | yumstock |
| **作者** | yumyumtum |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/yumyumtum-yumstock |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yumyumtum/yumstock |
| **安全评级** | 🟡 Medium |

## 功能概述
- SEC EDGAR filings (10-K, 10-Q)
- Yahoo Finance / Alpha Vantage style market data (price, volume, OHLC history)
- FRED macroeconomic indicators (WALCL, WTREGEN, RRPONTSYD, and others)
- CNN Fear and Greed Index: https://www.cnn.com/markets/fear-and-greed
- Chicago Fed NFCI: https://www.chicagofed.org/research/data/nfci/current-data
- Baltic Dry Index (BDI)
- ISM Manufacturing New Orders
- Conference Board US Leading Economic Index (LEI)

## 使用场景
- 管理食材库存和保质期
- 根据库存推荐可烹饪的菜品
- 生成采购清单和补货提醒

## 依赖和前提条件
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。Prompt 注入：发现 Prompt 注入特征

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
