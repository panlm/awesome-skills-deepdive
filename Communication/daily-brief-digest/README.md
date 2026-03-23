# Daily Brief Digest

> Generates a daily brief including urgent emails (himalaya), upcoming calendar events (gog), and relevant news. Use when the user asks for a morning summary, daily briefing, or a status update on their day.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Daily Brief Digest |
| **作者** | rajtejani61 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/rajtejani61-daily-brief-digest |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rajtejani61/daily-brief-digest |
| **安全评级** | 🟢 Low |

## 功能概述
- Email: `himalaya` CLI.
- Calendar: `gog` CLI.
- News: Web search or trusted RSS feeds.
- Logs: Saved locally to `~/.openclaw/cron/DailyDigest_logs/`.
- Google: Security alert (04:10)
- The Replit Team: Unlock Replit Agent's Full Potential (Feb 11)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23