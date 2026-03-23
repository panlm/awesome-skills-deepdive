# Control Chromecast

> 控制 Chromecast 设备 — 投屏、播放控制、设备发现

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Control Chromecast |
| **作者** | morozred |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/morozred-chromecast-control |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/morozred/chromecast-control |
| **安全评级** | 🟡 Medium |

## 功能概述
- Chromecast and computer must be on same network
- For local file casting: TCP ports 45000-47000 must be open
- Some networks block mDNS - use IP address directly if `catt scan` fails
- YouTube (videos, playlists, live streams)
- Vimeo, Dailymotion, Twitch
- Direct video URLs (MP4, MKV, WebM, etc.)
- Local files (video, audio, images)
- Hundreds more sites (see yt-dlp supported sites)

## 使用场景
- 在 Chromecast 上投屏播放视频和音频
- 控制 Chromecast 的播放、暂停和音量
- 管理多台 Chromecast 设备和播放队列

## 依赖和前提条件
- pip / uv 包管理器
- 数据库
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
