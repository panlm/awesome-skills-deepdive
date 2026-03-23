# Last.fm

> Last.fm 音乐数据和听歌记录工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Last.fm |
| **作者** | gumadeiras |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/gumadeiras-lastfm |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gumadeiras/lastfm |
| **安全评级** | 🟡 Medium |

## 功能概述
- First track with `@attr.nowplaying=true` is currently playing
- Returns: artist, track name, album, timestamp, images
- Returns: playcount, artist_count, track_count, album_count, registered date
- Adding `username` includes user's playcount for that artist
- No auth needed for read-only endpoints (just API key)
- Rate limit: be reasonable, no hard limit documented
- URL-encode artist/track/album names (spaces → `+` or `%20`)
- Images come in sizes: small, medium, large, extralarge

## 使用场景
- 获取 Last.fm 听歌历史和统计
- 发现音乐推荐和相似艺术家
- 跟踪音乐收听趋势

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
