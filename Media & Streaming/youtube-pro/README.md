# YouTube Pro

> YouTube 视频深度分析、转录和元数据提取

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
- Fetch transcript via `summarize`
- Use `gemini` (MiniPC) to analyze the core message, audience sentiment (via comments if available), and practical takeaways
- Use `yt-dlp` (MiniPC) to download specific segments
- Use `ffmpeg` to extract frames for visual analysis
- Brevity: Summarize long transcripts into "핵심 요약 5줄" first
- Actionable: Always add a "미스 김의 제언" (Miss Kim's Suggestion) at the end

## 使用场景
- 分析 YouTube 视频的内容和指标
- 提取视频转录文本和字幕
- 下载和处理 YouTube 视频片段

## 依赖和前提条件
- 数据库
- FFmpeg

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
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
