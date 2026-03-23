# Apple Music

> Apple Music MCP 服务集成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apple Music |
| **作者** | epheterson |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/epheterson-mcp-applemusic |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/epheterson/mcp-applemusic |
| **安全评级** | 🟡 Medium |

## 功能概述
- Manage playlists (create, add/remove tracks, list)
- Control playback (play, pause, skip, volume)
- Search catalog or library
- Add songs to library
- Access listening history or recommendations
- ❌ Catalog ID → Playlist (fails)
- ✅ Catalog ID → Library → Playlist (works)
- No catalog access - only library content

## 使用场景
- 通过 MCP 协议访问 Apple Music
- 搜索和播放 Apple Music 曲库
- 管理 Apple Music 播放列表

## 依赖和前提条件
- Python / pip
- macOS
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
