# Chromecast Control (Chromecast 控制)

> 控制本地网络上的 Chromecast 设备 — 发现、投屏、播放控制、队列管理

## 📖 描述

Chromecast Control 允许 AI 助手通过 `catt` (Cast All The Things) 命令行工具管理本地网络上的 Chromecast 和 Google Cast 设备。支持设备发现、URL/本地文件投屏、播放控制、音量调节和队列管理。

## ✨ 功能特点

- **设备发现**: 扫描网络上所有 Chromecast 设备
- **媒体投屏**: 支持 YouTube、Vimeo 及数百个 yt-dlp 支持的网站
- **本地文件投屏**: 直接投屏本地视频/音频文件
- **播放控制**: 播放、暂停、停止、跳转
- **音量控制**: 设置音量 (0-100)
- **队列管理**: 添加媒体到播放队列
- **状态保存/恢复**: 保存和恢复播放位置

## 🚀 使用方法

### 安装
```bash
clawhub install morozred/chromecast-control
```

### 前置要求
- `catt` (通过 pip 或 uv 安装)

### 快速参考
```bash
# 扫描设备
catt scan

# 投屏 YouTube 视频
catt cast "https://www.youtube.com/watch?v=VIDEO_ID"

# 投屏本地文件
catt cast ./video.mp4

# 播放/暂停
catt play / catt pause

# 查看状态
catt status

# 设置音量
catt volume 50

# 指定设备
catt -d "客厅电视" cast "URL"
```

## 🔒 安全评估

| 项目 | 状态 |
|------|------|
| ClawHub 页面 | [查看](https://clawskills.sh/skills/morozred-chromecast-control) |
| GitHub 源码 | [查看](https://github.com/openclaw/skills/tree/main/skills/morozred/chromecast-control) |
| 安全状态 | ⚠️ 待验证 (Suspicious) |

## 📚 附加资源

- [ClawSkills 页面](https://clawskills.sh/skills/morozred-chromecast-control)
- [GitHub 源码仓库](https://github.com/openclaw/skills/tree/main/skills/morozred/chromecast-control)
- [catt 项目主页](https://github.com/skorokithakis/catt)
- 作者: @morozred
