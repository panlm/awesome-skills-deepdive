# compression

> Pre-run prompt compression for iterative AI dev loops.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | compression |
| **作者** | trinitybotserver |
| **ClawHub** | https://clawskills.sh/skills/trinitybotserver-compression |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/trinitybotserver/compression |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- `trinity-compress.config.json` — rules + targets
- `scripts/trinity-compress.sh` — compression script
- Makefile snippet (optional): `optimize-prompts`, `optimize-undo`, etc.
- `.gitignore` snippet: ignore `*.bak`
- Installers:
- `scripts/install.ps1` (Windows)
- `scripts/install.sh` (bash)

## 依赖和前提条件

- bash 4+
- `jq`
- `bc`

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | 🟢 Benign |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟡 警告 | 注意: write code blocks, urls, file |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 2 项警告: 命令执行, 文件系统篡改。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
