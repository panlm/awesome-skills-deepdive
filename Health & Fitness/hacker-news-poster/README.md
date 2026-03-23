# Hacker News Poster

> Hacker News 自动发帖工具

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
- HN rate-limits submissions and comments. If you get a rate limit error, wait a few minutes
- Comments can only be edited within ~2 hours of posting
- The `submit` command returns the new item id and url on success
- Session cookies are stored in `~/.hn_cookies.txt` to avoid re-authenticating on every command. Delete this file to clear the session
- For reading HN (search, top stories, comments), use the existing `hacker-news` skill or the HN API directly. This skill is write-only

## 使用场景
- 自动发布内容到 Hacker News
- 管理帖子发布时间和策略
- 跟踪帖子的表现和评论

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
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
