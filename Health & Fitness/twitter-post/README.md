# Twitter Post

> Post tweets to Twitter/X via the official API v2 (OAuth 1.0a). Use when the user asks to tweet, post to Twitter/X, send a thread, reply to a tweet, or quote tweet. Supports single tweets, threads, replies, and quote tweets with automatic character weight validation.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Twitter Post |
| **作者** | sit-in |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/sit-in-twitter-post |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sit-in/twitter-post |
| **安全评级** | 🟡 Medium |

## 功能概述
- `HTTPS_PROXY` — HTTP proxy URL (e.g. `http://127.0.0.1:7897`) for regions that need it
- `TWITTER_DRY_RUN=1` — validate and print without posting
- Call `POST /oauth/request_token` with `oauth_callback=oob`
- User opens `https://api.twitter.com/oauth/authorize?oauth_token=<token>`
- User provides the PIN code
- Call `POST /oauth/access_token` with the PIN as `oauth_verifier`

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23