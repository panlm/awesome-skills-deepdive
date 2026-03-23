# omni stories

> 全渠道故事创作和发布工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | omni stories |
| **作者** | specter0o0 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/specter0o0-omni-stories |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/specter0o0/omni-stories |
| **安全评级** | 🔴 High |

## 功能概述
- High quality Narration: ElevenLabs tts integration (Free tier available)
- Local Fallback: if you don't have an API key or hit the quota limit, it will automatically fallback to use a tiny yet powerful local TTS (Kokoro-TTS) to generate the audio
- Modern Captions:: Accurate customizable captions, with perfect word-by-word synchronization and highlighting
- smart generation: You won't get repetitive background video clips, because the script automatically picks a random part of a random video you have in `background_videos/`. (I already have a non-copyrighted video ready for you!)
- no duplicates: Don't worry about your AI agent picking the same story over and over again. Each story will be stored in a local database file. The script won't accept stories that are already in the database
- Background videos: Easily download custom gameplay (or any video) via YouTube links
- Ready-to-upload: Automatically generates thumbnails and metadata for every story

## 使用场景
- 创作和编辑互动故事内容
- 发布故事到多个平台
- 管理故事库和创作素材

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
