# jarvis-voice

> JARVIS 风格 AI 语音助手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | jarvis-voice |
| **作者** | globalcaos |
| **ClawHub** | https://clawskills.sh/skills/globalcaos-jarvis-voice |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/globalcaos/jarvis-voice |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Jarvis: *Your spoken text here.*
- Backend: sherpa-onnx offline TTS (Alan voice, British English, `en_GB-alan-medium`)
- Speed: 2x (`--vits-length-scale=0.5`)
- Effects chain (ffmpeg):
- Pitch up 5% — tighter AI feel
- Flanger — metallic sheen

## 依赖和前提条件
- 
- `sherpa-onnx` runtime at `~/.openclaw/tools/sherpa-onnx-tts/`
- Alan medium model at `~/.openclaw/tools/sherpa-onnx-tts/models/vits-piper-en_GB-alan-medium/`
- `aplay` (ALSA) for audio playback
- The `jarvis` script at `~/.local/bin/jarvis` (or in PATH)

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `templates/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在动态代码执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🔴 High | 包含代码混淆或动态执行 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23