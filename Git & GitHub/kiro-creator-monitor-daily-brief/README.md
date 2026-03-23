# Kiro Creator Monitor Daily Brief

> 跨平台创作者话题监控，整合 X、RSS、GitHub 和 Reddit 信号，生成每日精选简报和社交媒体草稿。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Kiro Creator Monitor Daily Brief |
| **作者** | vmining |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/vmining-kiro-creator-monitor-daily-brief |

## 功能概述
- 从 X、RSS、GitHub、Reddit 等多源拉取创作者相关信号
- 自动去重和按相关性+新鲜度评分
- 输出每日 Top 5 精选简报
- 自动生成一篇可发布的 X/LinkedIn 社交草稿
- 支持定时推送到 Telegram、Slack 或邮箱
- 支持通过 JSON 配置话题关键词和排除词

## 使用场景
- 内容创作者每日跟踪行业话题和竞品动态
- 自动化社交媒体内容灵感收集和草稿准备
- 团队定时接收行业简报，提高信息同步效率

## 依赖和前提条件
- `python3`
- 环境变量：`X_BEARER_TOKEN`（X/Twitter 搜索必需）
- 可选环境变量：`TELEGRAM_BOT_TOKEN`、`TELEGRAM_CHAT_ID`、`SLACK_WEBHOOK_URL`
- 可选环境变量：`SMTP_HOST`、`SMTP_PORT`、`SMTP_USER`、`SMTP_PASS`、`EMAIL_TO`
- RSS 和公开 GitHub 端点可无需密钥运行

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
