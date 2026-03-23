# Podcast Generation from PDF, Text, and Links

> Generate AI podcast episodes from PDFs, text, notes, and links using MagicPodcast in OpenClaw. Creates natural two-person dialogue audio, supports custom language, and returns podcast links with progress tracking in the MagicPodcast dashboard. Use for PDF-to-podcast, text-to-podcast, and fast content-to-audio workflows.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Podcast Generation from PDF, Text, and Links |
| **作者** | mogens9 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/mogens9-ai-podcast |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mogens9/ai-podcast |
| **安全评级** | 🟡 Medium |

## 功能概述
- Signed-in users can generate free podcast.
- Expected generation time is usually 2-5 minutes.
- Right after starting, direct users to `https://www.magicpodcast.app/app`.
- Tell the user this page is their dashboard: they can see created podcasts, live progress/status, and finished episodes.
- Return `outputs.shareUrl` as the default completion link.
- If `outputs.shareUrl` is missing, fall back to `outputs.appUrl`.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `PUBLISH.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23