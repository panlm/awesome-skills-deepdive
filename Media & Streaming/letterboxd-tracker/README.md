# letterboxd-companion

> Your personal movie assistant. Track what you watch, check your lists, and get movie info from Letterboxd instantly.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | letterboxd-companion |
| **作者** | tamil-9421 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/tamil-9421-letterboxd-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tamil-9421/letterboxd-tracker |
| **安全评级** | 🟢 Low |

## 功能概述
- User Stats: Get a user's watched count, reviews, lists, and favorite movies.
- Diary: Fetch recently watched movies from a user's diary.
- Watchlist: Retrieve movies from a user's watchlist.
- Movie Details: Get information about a specific movie (directors, year, rating).

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `lb_tool.py`
- `requirements.txt`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23