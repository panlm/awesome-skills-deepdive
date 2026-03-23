# audio-reply

> 使用 TTS 生成语音回复，支持朗读网页内容和语音对话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | audio-reply |
| **作者** | matrixy |
| **ClawHub** | https://clawskills.sh/skills/matrixy-audio-reply-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matrixy/audio-reply-skill |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- "read it to me [URL]" - Fetches public web content from a URL and reads it aloud
- "talk to me [topic]" - Generates a conversational spoken response
- "speak" / "say it" / "voice reply" - Converts any response to audio
- macOS with Apple Silicon (M1/M2/M3/M4)
- model mlx-community/chatterbox-turbo-fp16 \
- text "Hello, testing audio." \

## 依赖和前提条件
- macOS with Apple Silicon (M1/M2/M3/M4)
- [Claude Code](https://claude.ai/claude-code) CLI
- [uv](https://github.com/astral-sh/uv) package manager
- Copy the skill to your Claude Code skills directory**:
- First run will auto-download the model** (~500MB):

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件删除操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23