# music-generator

> Generates music from a structured Composition Plan. Use this skill to execute music generation after a prompt or plan has been designed. It validates the output quality and retries on failure.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | music-generator |
| **作者** | wells1137 |
| **ClawHub** | https://clawskills.sh/skills/wells1137-music-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wells1137/music-generator |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- **After a `Composition Plan` is created**: This skill is the logical next step once you have a detailed JSON plan for the music.
- **To execute music generation**: When the goal is to produce the final audio file based on a prompt or design.
- The `Composition Plan` has not been created or is incomplete.
- You only need to design the music, not generate it (use a `music-design` or `prompt-generation` skill for that).
- **Specification-Driven**: Generation parameters must strictly match the design specifications in the `Composition Plan`.
- **Duration Precision**: The output audio's duration must be validated against the target length with a tight tolerance.

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 未检测到命令执行相关风险模式 |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟡 警告 | 注意: automatically |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 1 项警告: Prompt 注入。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
