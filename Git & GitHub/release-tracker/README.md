# Release Tracker

> 追踪 GitHub 仓库的新版本发布，生成优先级摘要并推送到多个通知渠道

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Release Tracker |
| **作者** | jo9900 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jo9900-release-tracker |

## 功能概述
- 监控一个或多个 GitHub 仓库的新版本发布
- 基于自定义优先级关键词生成排序摘要
- 多渠道消息推送：Discord（论坛帖子或频道消息）、Telegram、Slack、纯文本
- 支持 JSON 配置文件管理多仓库监控
- 独立版本状态追踪，避免重复通知
- 可配置定时任务（cron job）实现自动化检查
- 支持预发布版本的包含/排除

## 使用场景
- 自动监控关键开源项目的新版本发布，第一时间获得通知
- 为团队设置多仓库 Release 监控，推送到 Discord/Slack 频道
- 生成 Changelog 摘要，重点突出关注的功能关键词

## 依赖和前提条件
- GitHub CLI（`gh`）已安装并认证
- 对应通知渠道的 OpenClaw 配置（Discord/Telegram/Slack）

## 安全状态
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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23