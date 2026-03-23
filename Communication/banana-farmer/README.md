# Banana Farmer

> Stock momentum scanner and portfolio intelligence. Look up any ticker for momentum scores, RSI, coil breakout patterns, and AI analysis. Scan top signals across 6,500+ stocks and crypto. Track portfolio holdings with real-time alerts. Market pulse, sector trends, win/loss proof data, and risk assessment — all through natural conversation. Powered by 730 days of backtested data with an 80% 5-day win rate.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Banana Farmer |
| **作者** | adamandjarvis |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/adamandjarvis-banana-farmer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/adamandjarvis/banana-farmer |
| **安全评级** | 🟡 Medium |

## 功能概述
- "What's the momentum on AAPL?"
- "Look up TSLA for me"
- "How's Bitcoin looking?"
- "Check NVDA's score and technicals"
- "Is CRWV ripe?"
- "What's the coil score on AMD?"

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23