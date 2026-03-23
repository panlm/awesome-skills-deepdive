# Kalshi Agent

> Kalshi 预测市场交易代理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Kalshi Agent |
| **作者** | jthomasdevs |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/jthomasdevs-kalshi-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jthomasdevs/kalshi-agent |
| **安全评级** | 🟡 Medium |

## 功能概述
- If many series match, shows an interactive numbered list — enter a number to drill into that series' markets
- If few series match, fetches and displays markets directly
- Prices are in cents (68 = $0.68 = 68% implied probability)
- Prices display as both dollars and percentages (e.g. `$0.68 (68%)`)
- Expiry times are human-readable: "8h 35m", "Fri 04:00PM", "Apr 01", "Jan 01, 2027"
- Event tickers start with `KX` (e.g. `KXWO-GOLD-26`); market tickers have more segments (e.g. `KXWO-GOLD-26-NOR`)
- Market tables show outcome names (e.g. "Norway" instead of raw tickers) when available

## 使用场景
- 自动化 Kalshi 预测市场交易
- 分析预测市场事件和概率
- 管理预测市场投资组合

## 依赖和前提条件
- Node.js / npm
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `install.sh`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
