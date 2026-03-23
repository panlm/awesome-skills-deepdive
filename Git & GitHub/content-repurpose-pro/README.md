# Content Repurposer

> When user asks to repurpose content, convert blog to tweets, turn article into LinkedIn post, create Twitter thread from text, make Instagram caption from blog, convert content to email newsletter, create YouTube description from script, generate TL;DR from article, turn podcast notes into posts, or any content format conversion task. 15-feature AI content repurposer that transforms one piece of content into 7+ formats. All data stays local — NO external API calls, NO network requests, NO data sent to any server. Does NOT post to any platform — generates text for user to copy.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Content Repurposer |
| **作者** | mkpareek0315 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/mkpareek0315-content-repurpose-pro |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mkpareek0315/content-repurpose-pro |
| **安全评级** | 🟢 Low |

## 功能概述
- `settings.json` — preferences and stats
- `history.json` — repurposed content log
- `saved.json` — bookmarked outputs
- Only reads/writes files under `~/.openclaw/content-repurposer/`
- Makes NO external API calls or network requests
- Sends NO data to any server, email, or messaging service

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23