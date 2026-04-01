# mlx-tts

> 使用 MLX 框架进行本地文字转语音

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | mlx-tts |
| **作者** | guoqiao |
| **ClawHub** | https://clawskills.sh/skills/guoqiao-mlx-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/guoqiao/mlx-tts |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- "/mlx-tts <text>"
- "Convert text to audio ..."
- "Say <text>"
- "Reply with voice message ..."

## 使用场景

Runs text-to-speech on Apple Silicon using MLX and open-source models (default QWen3-TTS). Generates audio files locally with no API key or external server needed. Works only on macOS with Apple Silicon.

## 依赖和前提条件

- macOS 系统

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未通过或状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: bash
bash ${baseDir}/install.sh
, bash
bash ${baseDir}/mlx-tts.sh "<text>"
, bash path/to/mlx-tts.sh "hello world" |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟡 警告 | 涉及凭证/令牌使用但未直接读取凭证文件 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 仅在工作目录内进行文件操作 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 2 项警告，无严重风险。执行 shell 命令: bash
bash ${baseDir}/install.sh
, bas

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
