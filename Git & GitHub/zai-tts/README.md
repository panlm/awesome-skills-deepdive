# 🗣️ Text-to-speech using GLM-TTS for generating audio

> 通过 GLM-TTS 服务将文本转换为高质量语音，支持预克隆声音和多种使用场景

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | 🗣️ Text-to-speech using GLM-TTS for generating audio |
| **作者** | al-one |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/al-one-zai-tts |

## 功能概述
- 使用 `uvx zai-tts` 命令将文本转换为语音音频
- 支持预克隆声音（pre-cloned voices）进行个性化语音合成
- 适用于多任务处理、无障碍访问、播客制作等场景
- 通过 "tts" 关键词触发语音合成
- 基于 GLM-TTS 服务，生成高质量语音输出

## 使用场景
- 将文字内容转为语音播放（如驾驶、烹饪时的免手操作场景）
- 使用克隆声音生成个性化语音内容（如播客、有声读物）
- 为无障碍需求提供文本朗读服务

## 依赖和前提条件
- `uvx` 工具（通过 Homebrew 安装 `uv`：`brew install uv`，或通过 pip：`pip install uv`）
- 环境变量 `ZAI_AUDIO_USERID`：登录 audio.z.ai 后从浏览器控制台获取
- 环境变量 `ZAI_AUDIO_TOKEN`：登录 audio.z.ai 后从浏览器控制台获取

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
