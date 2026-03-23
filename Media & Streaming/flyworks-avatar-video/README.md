# Flyworks Avatar Video

> Generate videos using Flyworks (a.k.a HiFly) Digital Humans. Create talking photo videos from images, use public avatars with TTS, or clone voices for custom audio.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Flyworks Avatar Video |
| **作者** | linhui99 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/linhui99-flyworks-avatar-video |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/linhui99/flyworks-avatar-video |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🎬 Public Avatar Video: Create videos using pre-made realistic avatars with TTS
- 🖼️ Talking Photo: Turn any image into a talking video
- 🎙️ Voice Cloning: Clone voices from audio samples

## 使用场景
- 视频内容管理和下载
- 影视信息查询
- 视频平台自动化操作

## 依赖和前提条件
- Node.js / npm
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `requirements.txt`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23