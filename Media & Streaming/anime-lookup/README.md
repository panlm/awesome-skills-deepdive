# Anime

> "CLI for AI agents to search and lookup anime info for their humans. Uses Jikan (unofficial MyAnimeList API). No auth required."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Anime |
| **作者** | jeffaf |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/jeffaf-anime-lookup |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jeffaf/anime-lookup |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🔍 Search anime by title
- 📊 Get detailed info (synopsis, score, episodes, genres, studios)
- 📺 Browse current season
- 🏆 View top ranked anime
- 📅 Check upcoming releases
- 🎯 No API key or account required

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23