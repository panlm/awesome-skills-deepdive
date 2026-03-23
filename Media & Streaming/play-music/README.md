# Play Local Music

> **Controlled music player with pause/resume/stop support**

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Play Local Music |
| **作者** | awspace |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/awspace-play-music |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/awspace/play-music |
| **安全评级** | 🟡 Medium |

## 功能概述
- Music directory: `./music` (relative to script location)
- Default song: `jaychou-sunnyday.mp3` (or set via DEFAULT_SONG)
- Lock file: `/tmp/music_player.lock` (for server coordination)

## 使用场景
- 音频内容播放和管理
- 文本转语音功能
- 音乐库搜索和控制

## 依赖和前提条件
- Python / pip
- macOS

## 包含文件
- `ORIGINAL_README.md`
- `SETUP.md`
- `SKILL.md`
- `_meta.json`
- `music-server.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。供应链风险：需要安装外部包且含管道安装；文件系统篡改：涉及危险文件操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23