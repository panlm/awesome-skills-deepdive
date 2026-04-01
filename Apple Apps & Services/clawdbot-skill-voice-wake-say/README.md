# clawdbot-skill-voice-wake-say

> 语音唤醒并朗读 ClawdBot 响应

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | clawdbot-skill-voice-wake-say |
| **作者** | xadenryan |
| **ClawHub** | https://clawskills.sh/skills/xadenryan-clawdbot-skill-voice-wake-say |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xadenryan/clawdbot-skill-voice-wake-say |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- **Step 1:** Acknowledge with `say` first (so the user knows you heard them)
- **Step 2:** Then perform the task
- **Step 3:** Optionally speak again when done if it makes sense
- THEN: Do NOT use `say`. Text-only response only.
- Check EACH message individually — context does NOT carry over
- The trigger phrase must be at the VERY START of the message
- For tasks that take time, acknowledge FIRST so the user knows you're working
- Trigger ONLY when the latest user/system message STARTS WITH `User talked via voice recognition on m3`

## 使用场景

Reads assistant responses aloud on macOS using the built-in `say` command. Triggers only when the user message starts with the exact phrase \

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
| SEC-01 命令执行 | 🟡 警告 | 执行 shell 命令: 
- If the message instructs "repeat prompt first", keep that behavior in the response.

2) Prepare spoken text
- Use the final response text as the basis.
- Strip markdown/code blocks; if the response is long or code-heavy, speak a short summary and mention that details are on screen.

3) Speak with , bash
printf '%s' "$SPOKEN_TEXT" | say
, bash
printf '%s' "$SPOKEN_TEXT" | say -v "$SAY_VOICE"
printf '%s' "$SPOKEN_TEXT" | say -r "$SAY_RATE"
 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络数据发送行为 |
| SEC-03 凭证获取 | 🟢 通过 | 不涉及任何凭证或密钥操作 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无文件系统修改行为 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境信息 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 发现 1 项警告，无严重风险。执行 shell 命令: 
- If the message instructs "repeat p

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:44 UTC
