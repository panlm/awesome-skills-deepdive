# clawtunes

> OpenClaw 音乐播放和管理插件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawtunes |
| **作者** | forketyfork |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/forketyfork-clawtunes |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/forketyfork/clawtunes |
| **安全评级** | 🟢 Low |

## 功能概述
- Install (Homebrew): `brew install forketyfork/tap/clawtunes`
- macOS-only; requires Apple Music app
- Play a song: `clawtunes play song "Song Name"`
- Play an album: `clawtunes play album "Album Name"`
- Play a playlist: `clawtunes play playlist "Playlist Name"`
- Always use the `--non-interactive` (`-N`) flag to prevent interactive prompts: `clawtunes -N play song "Song Name"`
- If the command exits with code 1 and lists multiple matches, retry with a more specific song/album/playlist name
- If a more specific name still returns multiple matches, use the `--first` (`-1`) flag to auto-select the first result: `clawtunes -1 play song "Song Name"`

## 使用场景
- 播放和管理本地音乐库
- 创建和编辑播放列表
- 集成音乐流媒体服务

## 依赖和前提条件
- macOS
- Homebrew

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
