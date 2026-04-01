# acestep-lyrics-transcription

> 使用 OpenAI Whisper 或 ElevenLabs Scribe API 将音频转录为带时间戳的歌词文件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | acestep-lyrics-transcription |
| **作者** | dumoedss |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/dumoedss-acestep-lyrics-transcription |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dumoedss/acestep-lyrics-transcription |
| **安全评级** | 🔴 High |

## 功能概述
- 支持将音频文件转录为 LRC、SRT 或 JSON 格式的带时间戳歌词
- 支持 OpenAI Whisper 和 ElevenLabs Scribe 两种转录引擎
- 提供词级别（word-level）的精确时间戳标注
- 内置 API Key 配置检查和引导流程
- 支持自动纠正误识别的歌词文本
- 提供可配置的转录参数和输出格式选项

## 使用场景
- 将歌曲音频自动转录为 LRC 歌词文件，用于音乐播放器同步显示
- 为播客或演讲音频生成 SRT 字幕文件
- 批量处理音乐库，为每首歌曲生成对应的时间戳歌词

## 依赖和前提条件
- Python 3.x
- OpenAI API Key（Whisper 引擎）或 ElevenLabs API Key（Scribe 引擎）
- Bash 脚本执行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
