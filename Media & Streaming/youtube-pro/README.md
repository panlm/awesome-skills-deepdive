# YouTube Pro

> Advanced YouTube analysis, transcripts, and metadata extraction.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | YouTube Pro |
| **作者** | kjaylee |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/kjaylee-youtube-pro |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kjaylee/youtube-pro |
| **安全评级** | 🟢 Low |

## 功能概述
- Summary: `summarize "URL"`
- Transcript: `summarize "URL" --youtube auto --extract-only`
- Fetch transcript via `summarize`.
- Use `gemini` (MiniPC) to analyze the core message, audience sentiment (via comments if available), and practical takeawa
- Use `yt-dlp` (MiniPC) to download specific segments.
- Use `ffmpeg` to extract frames for visual analysis.

## 使用场景
- 视频内容管理和下载
- 影视信息查询
- 视频平台自动化操作

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23