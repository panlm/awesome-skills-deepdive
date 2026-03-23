# MH openai-whisper

> 使用本地 Whisper CLI 进行语音转文字，无需 API Key

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | MH openai-whisper |
| **作者** | mohdalhashemi98-hue |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/mohdalhashemi98-hue-mh-openai-whisper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mohdalhashemi98-hue/mh-openai-whisper |
| **安全评级** | 🟢 Low |

## 功能概述
- 完全本地运行的语音转文字工具，保护隐私
- 支持多种音频格式（mp3、m4a 等）
- 支持转录和翻译两种任务模式
- 多种模型大小可选，平衡速度与准确性
- 支持多种输出格式（txt、srt 等）
- 模型首次运行时自动下载到 ~/.cache/whisper

## 使用场景
- 将播客或采访录音快速转录为文字稿
- 为视频生成 SRT 字幕文件
- 在无网络环境下进行本地语音转文字处理

## 依赖和前提条件
- Whisper CLI（可通过 brew install openai-whisper 安装）
- 足够的磁盘空间用于模型缓存

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
