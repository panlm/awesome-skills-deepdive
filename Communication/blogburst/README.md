# BlogBurst - Virtual CMO Agent

> Your AI Chief Marketing Officer. Autonomous agent that runs your entire marketing — auto-posts to Twitter/X, Bluesky, Telegram, Discord, auto-engages with your audience (replies, likes, follows), runs SEO/GEO audits, tracks competitors, scans communities for opportunities, learns what works, and continuously optimizes. 50+ countries, 1000+ posts published. Free tier available.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BlogBurst - Virtual CMO Agent |
| **作者** | shensi8312 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/shensi8312-blogburst |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shensi8312/blogburst |
| **安全评级** | 🟡 Medium |

## 功能概述
- Blog Generation: Give it a topic, get a full blog post with title, content, meta description, and tags
- Content Repurposing: Paste a URL or text → get ready-to-post content for Twitter, LinkedIn, Reddit, Threads, Bluesky, an
- Trending Topics: Discover what's hot on HackerNews, Reddit, Google Trends, and Product Hunt — filtered by your niche
- Multi-Platform: Supports 9 platforms with platform-specific formatting and character limits

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key
- OAuth

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23