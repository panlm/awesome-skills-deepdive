# Apple Music (Apple Music 集成)

> 通过 AppleScript (macOS) 或 MusicKit API 集成 Apple Music

## 📖 描述

Apple Music Integration 是一个 MCP 服务器技能，用于在 macOS 上控制 Apple Music 以及通过 MusicKit API 进行跨平台集成。支持 AppleScript 执行、令牌管理、播放列表管理、目录搜索和播放控制。

## ✨ 功能特点

- **播放控制**: 播放、暂停、跳过、音量调节
- **播放列表管理**: 创建、添加/删除曲目、列出播放列表
- **目录搜索**: 通过 MusicKit API 搜索歌曲
- **资料库管理**: 添加歌曲到资料库
- **收听历史**: 获取最近播放和推荐
- **双模式支持**: AppleScript (零配置) + MusicKit API (跨平台)

## ⚠️ 关键规则: Library-First 工作流

**不能**直接将目录歌曲添加到播放列表！

歌曲必须先在用户资料库中：
- ❌ Catalog ID → 播放列表 (失败)
- ✅ Catalog ID → 资料库 → 播放列表 (成功)

## 🚀 使用方法

### 安装
```bash
clawhub install epheterson/mcp-applemusic
```

### 前置要求
- Apple Developer 账号 ($99/年) - 用于 MusicKit API
- MusicKit 私钥 (.p8 文件)
- Apple Music 订阅

### 平台对比

| 功能 | AppleScript (macOS) | MusicKit API |
|------|:---:|:---:|
| 需要配置 | 无 | 开发者账号 + 令牌 |
| 播放列表管理 | 完整 | 仅 API 创建的 |
| 播放控制 | 完整 | 无 |
| 目录搜索 | 否 | 是 |
| 跨平台 | 否 | 是 |

## 🔒 安全评估

| 项目 | 状态 |
|------|------|
| ClawHub 页面 | [查看](https://clawskills.sh/skills/epheterson-mcp-applemusic) |
| GitHub 源码 | [查看](https://github.com/openclaw/skills/tree/main/skills/epheterson/mcp-applemusic) |
| 安全状态 | ⚠️ 待验证 (Suspicious) |

## 📚 附加资源

- [ClawSkills 页面](https://clawskills.sh/skills/epheterson-mcp-applemusic)
- [GitHub 源码仓库](https://github.com/openclaw/skills/tree/main/skills/epheterson/mcp-applemusic)
- [Apple MusicKit 文档](https://developer.apple.com/musickit/)
- 作者: @epheterson
