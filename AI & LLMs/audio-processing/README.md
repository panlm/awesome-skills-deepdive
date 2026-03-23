# Audio Processing

> 综合音频处理工具集，支持语音转录、文字转语音、语音活动检测和音频特征提取。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Audio Processing |
| **作者** | iyeque |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/iyeque-audio-processing |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iyeque/audio-processing |
| **安全评级** | 🟢 Low |

## 功能概述
- 语音转录（Transcribe）：使用 OpenAI Whisper 将音频转为文字
- 文字转语音（TTS）：使用 gTTS 将文本转为语音文件
- 语音活动检测（VAD）：识别音频中的语音片段
- 音频特征提取：使用 librosa 分析音频特征
- 音频格式转换和处理
- 内置安全验证：路径遍历防护、系统目录访问阻止、文本长度限制

## 使用场景
- 为 AI Agent 添加语音转文字能力，处理会议录音或语音消息
- 生成语音播报内容，如新闻摘要或通知朗读
- 分析音频文件特征，用于音乐推荐或声音分类

## 依赖和前提条件
- 需要 `ffmpeg` 和 `python3`
- 需要 pip 安装：`openai-whisper`、`gTTS`、`librosa`、`pydub`、`soundfile`、`numpy`、`webrtcvad-wheels`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
