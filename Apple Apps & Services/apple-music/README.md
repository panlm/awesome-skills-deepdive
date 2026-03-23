# apple-music

> 搜索 Apple Music、添加歌曲、管理播放列表和 AirPlay 控制

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | apple-music |
| **作者** | tyler6204 |
| **ClawHub** | https://clawskills.sh/skills/tyler6204-apple-music |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tyler6204/apple-music |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Playback: `./apple-music.sh player [now|play|pause|toggle|next|prev|shuffle|repeat|volume N|song "name"]`
- AirPlay: `./apple-music.sh airplay [list|select N|add N|remove N]`
- Portal steps first:
- Then run setup:
- ⚠️ Agents: Always use `./launch-setup.sh` to open Terminal. Don't run setup.sh through chat (requires interactive input).
- 401: Token expired, re-run setup

## 依赖和前提条件
- Playback:** `./apple-music.sh player [now|play|pause|toggle|next|prev|shuffle|repeat|volume N|song "name"]`
- AirPlay:** `./apple-music.sh airplay [list|select N|add N|remove N]`
- Portal steps first:**
- developer.apple.com → Keys → Create MusicKit key → Download .p8
- Note your Key ID and Team ID

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `apple-music.sh` — 脚本文件
- `auth.html`
- `launch-setup.sh` — 脚本文件
- `lib/` — 目录
- `setup.sh` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23