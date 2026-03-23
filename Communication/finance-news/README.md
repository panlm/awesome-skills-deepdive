# Finance News Briefings

> "Market news briefings with AI summaries. Use when asked about stock news, market updates, portfolio performance, morning/evening briefings, financial headlines, or price alerts. Supports US/Europe/Japan markets, WhatsApp delivery, and English/German output."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Finance News Briefings |
| **作者** | kesslerio |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-finance-news |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/finance-news |
| **安全评级** | 🔴 High |

## 功能概述
- Multi-source aggregation: Reuters, WSJ, FT, Bloomberg, CNBC, Yahoo Finance, Tagesschau, Handelsblatt
- Global markets: US (S&P, Dow, NASDAQ), Europe (DAX, STOXX, FTSE), Japan (Nikkei)
- AI summaries: LLM-powered analysis in German or English
- Automated briefings: Morning (market open) and evening (market close)
- WhatsApp/Telegram delivery: Send briefings via openclaw
- Portfolio tracking: Personalized news for your stocks with price alerts
- Lobster workflows: Approval gates before sending

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- Docker
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `config`
- `docs`
- `htmlcov`
- `pyproject.toml`
- `pytest.ini`
- `requirements-test.txt`
- `requirements.txt`
- `scripts`
- `tests`
- `workflows`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，5 项中风险。持久化机制：设置系统级持久化；信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23