# Apple Media Remote (for HomePod, Apple TV, etc)

> Apple Music 和 Apple 媒体服务集成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apple Media Remote (for HomePod, Apple TV, etc) |
| **作者** | aaronn |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/aaronn-apple-media |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aaronn/apple-media |
| **安全评级** | 🟢 Low |

## 功能概述
- pyatv has a compatibility issue with Python 3.14+. Use `--python python3.13` (or any version ≤3.13) when installing
- If `~/.local/bin` isn't on your PATH after install, run: `pipx ensurepath`
- If your default Python is 3.14+, you can also call directly: `python3.13 -m pyatv.scripts.atvremote <command>`
- Pause vs Stop: Use `pause`/`play` to suspend and resume. `stop` ends the session entirely — playback must be restarted from the source (Siri, Home app, etc.)
- HomePods with "Pairing: NotNeeded" can be streamed to immediately
- Apple TVs typically require pairing first (all protocols the device supports)
- The `playing` command shows media type, title, artist, position, shuffle/repeat state
- For stereo HomePod pairs, target either unit by name

## 使用场景
- 搜索和播放 Apple Music 曲库
- 管理 Apple 媒体订阅和播放列表
- 获取 Apple 平台上的媒体元数据

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
