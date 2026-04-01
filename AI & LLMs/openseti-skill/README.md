# openseti-skill

> Distributed SETI scanner - contribute compute power to analyze real radio telescope data from Breakthrough Listen. Earn tokens when your analysis discovers anomalies. Use when setting up distributed alien signal detection, running SETI scans, or contributing to the OpenSETI network.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | openseti-skill |
| **作者** | synergysize |
| **ClawHub** | https://clawskills.sh/skills/synergysize-openseti-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/synergysize/openseti-skill |
| **安全评级** | 🟢 Low (低风险) |

## 功能概述

- **Narrowband signals** (< 10 Hz bandwidth) - Natural sources are broadband
- **Doppler drift** - Frequency shift indicating non-terrestrial origin
- **High SNR** - Strong signals above noise floor
- **Hydrogen line proximity** - 1420.405 MHz is the "water hole"
- **Non-RFI patterns** - Doesn't match known Earth interference
- `openseti register <wallet>` - Register your Solana wallet

## 依赖和前提条件

- Python 3.8+
- NumPy and SciPy (`pip install numpy scipy requests`)

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 警告 | 注意: bash |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: pip install |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟢 Low (低风险)**

**风险摘要:** 检测到 2 项警告: 命令执行, 供应链风险。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
