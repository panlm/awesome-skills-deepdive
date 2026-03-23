# Her Voice

> 个性化 AI 语音助手，类似《Her》电影风格

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Her Voice |
| **作者** | matusvojtek |
| **ClawHub** | https://clawskills.sh/skills/matusvojtek-her-voice |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matusvojtek/her-voice |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Give your agent a voice. Audio responses powered by Kokoro TTS — a compact, naturally expressive model running entirely on-device.
- ⚡ On-the-fly Streaming — Audio plays as it generates, very low latency
- 👄 The Voice of an angel — Cutting-edge local text-to-speech model Kokoro TTS
- 🧠 TTS Daemon — Keep the model warm in RAM for instant responses (can be disabled to save RAM)
- 🖥️ Persist Mode — Drag & drop audio, paste text, use as a voice station
- 🔧 Fully Configurable — Voice, speed, visualizer, notification sounds

## 依赖和前提条件
- Detect platform and select TTS engine (MLX on Apple Silicon, PyTorch elsewhere)
- TTS pronunciation tip:** If the user's name is non-English, figure out a phonetic English spelling that Kokoro will pronounce correctly. Store it in `user_name_tts` and use that spelling whenever speaking the name aloud. The real name stays in `user_name` for display purposes.
- macOS + Apple Silicon** recommended for best experience (MLX engine + visualizer + notification sounds)
- Linux/Intel Mac** supported via PyTorch Kokoro engine (no visualizer)
- Windows** is not supported

## 包含文件
- `CHANGELOG.md`
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `assets/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 包含高危系统命令 |
| SEC-02 数据外泄 | 🟡 Medium | 存在网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件删除操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23