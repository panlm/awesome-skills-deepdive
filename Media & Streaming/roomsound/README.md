# RoomSound

> RoomSound gives your agent the skill to play audio to your speakers. Starting with YouTube to Bluetooth speakers, expanding to local files and other sources.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | RoomSound |
| **作者** | icecat2005 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/icecat2005-roomsound |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/icecat2005/roomsound |
| **安全评级** | 🟡 Medium |

## 功能概述
- Device discovery: `bluetoothctl paired-devices`, `bluetoothctl info <MAC>`, `wpctl status`, `pactl list short sinks`
- Speaker switching: `bluetoothctl devices Connected`, `bluetoothctl disconnect <MAC>`, `bluetoothctl connect <MAC>`
- YouTube playback: `mpv --no-video "<url>"` and `yt-dlp` search/print commands
- Queue-first playback: build a contextual queue unless the user explicitly requests a specific list/order
- Run one-time validation:
- Persist config:

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `QUICK-START-GUIDE.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23