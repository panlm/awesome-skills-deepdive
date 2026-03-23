# yahooquery

> Access Yahoo Finance data including real-time pricing, fundamentals, analyst estimates, options, news, and historical data via the yahooquery Python library.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | yahooquery |
| **作者** | 512z |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/512z-yahooquery |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/512z/yahooquery |
| **安全评级** | 🟡 Medium |

## 功能概述
- `.income_statement(frequency='a', trailing=True)` - Income statement (annual/quarterly)
- `.balance_sheet(frequency='a', trailing=True)` - Balance sheet
- `.cash_flow(frequency='a', trailing=True)` - Cash flow statement
- `.all_financial_data(frequency='a')` - Combined financials + valuation measures
- `.valuation_measures` - EV/EBITDA, P/E, P/B, P/S across periods
- `.price` - Current pricing, market cap, 52-week range

## 使用场景
- 管理 macOS/iOS 日历事件
- 查询日程安排与空闲时间
- 通过命令行创建/修改日历事件

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23