# omni stories

> Omni Stories is a skill that allows AI agents to generate narrated Reddit stories on background videos with modern captions. (all free!)

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
- High quality Narration: ElevenLabs tts integration (Free tier available).
- Local Fallback: if you don't have an API key or hit the quota limit, it will automatically fallback to use a tiny yet po
- Modern Captions:: Accurate customizable captions, with perfect word-by-word synchronization and highlighting.
- smart generation: You won't get repetitive background video clips, because the script automatically picks a random part 
- no duplicates: Don't worry about your AI agent picking the same story over and over again. Each story will be stored in 
- Background videos: Easily download custom gameplay (or any video) via YouTube links.
- Ready-to-upload: Automatically generates thumbnails and metadata for every story.

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
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