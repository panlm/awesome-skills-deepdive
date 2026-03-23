# mediaproc

> Process media files (video, audio, images) via a locked-down SSH container with ffmpeg, sox, and imagemagick. Use when the user wants to transcode video, process audio, manipulate images, or work with media files.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mediaproc |
| **作者** | psyb0t |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/psyb0t-mediaproc |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/psyb0t/mediaproc |
| **安全评级** | 🟡 Medium |

## 功能概述
- frei0r — Video effect plugins (used via `-vf frei0r=...`)
- LADSPA — Audio effect plugins: SWH, TAP, CMT (used via `-af ladspa=...`)
- LV2 — Audio plugins (used via `-af lv2=...`)

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- Docker

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23