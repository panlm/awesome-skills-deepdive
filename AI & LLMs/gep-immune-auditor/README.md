# gep-immune-auditor

> Security audit agent for GEP/EvoMap ecosystem. Scans Gene/Capsule assets using immune-system-inspired 3-layer detection: L1 pattern scan, L2 intent inference, L3 propagation risk. Rates findings CLEAN/SUSPECT/THREAT/CRITICAL. Publishes discovered malicious patterns to EvoMap as Gene+Capsule bundles.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | gep-immune-auditor |
| **作者** | andyxinweiminicloud |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-gep-immune-auditor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/gep-immune-auditor |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- A2A_HUB_URL
- Cross-Capsule dependency chain analysis: does the chain include flagged assets?
- Publish frequency anomaly: mass publish from one node (like abnormal cell proliferation)
- Clone detection: near-duplicate Capsules washing IDs to bypass SHA-256 dedup
- **Declared vs actual behavior**: summary says "fix SQL injection" — does the code actually fix it?
- **Permission creep**: does fixing one bug require reading `.env`? calling `subprocess`?

## 依赖和前提条件

- 无特殊依赖

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟡 Suspicious |

> ⚠️ ClawHub 安全扫描未全部通过，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 危险 | 检测到: subprocess |
| SEC-02 数据外泄 | 🟢 通过 | 未检测到数据外泄相关风险模式 |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟢 通过 | 未检测到供应链风险相关风险模式 |
| SEC-05 文件系统篡改 | 🟢 通过 | 未检测到文件系统篡改相关风险模式 |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟡 警告 | 注意: list all |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟢 通过 | 未检测到信息采集相关风险模式 |
| SEC-10 混淆/反分析 | 🟡 警告 | 注意: base64, encode |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到以下高风险项: 命令执行。 另有 2 项警告。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
