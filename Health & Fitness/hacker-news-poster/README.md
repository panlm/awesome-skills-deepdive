# Hacker News Poster

> Post, comment, and interact on Hacker News. Use when the user asks to submit a Show HN, post a story, comment on an HN thread, edit a comment, or update an HN profile. Requires HN_USERNAME and HN_PASSWORD environment variables. Persists session cookies to ~/.hn_cookies.txt (configurable via HN_COOKIE_FILE env var).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hacker News Poster |
| **作者** | saikatkumardey |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/saikatkumardey-hacker-news-poster |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/saikatkumardey/hacker-news-poster |
| **安全评级** | 🟡 Medium |

## 功能概述
- HN rate-limits submissions and comments. If you hit a limit, wait a few minutes.
- Pair with the read-only [hacker-news](https://clawhub.com/skills/hacker-news) skill for browsing/searching.

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
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
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23