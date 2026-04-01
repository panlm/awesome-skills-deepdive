# ecommerce-price-monitor

> This skill enables Claude to monitor and track **product prices across major e-commerce platforms**

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | ecommerce-price-monitor |
| **作者** | g4dr |
| **ClawHub** | https://clawskills.sh/skills/g4dr-ecommerce-price-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/g4dr/ecommerce-price-monitor |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- Monitor product prices on **Amazon**, **Zalando**, **eBay**, **AliExpress**, and more
- Track price history and detect **drops, spikes, and promotions**
- Compare prices for the same product **across multiple retailers**
- Trigger **repricing alerts** when a competitor changes their price
- Build structured price datasets for dashboards and analytics
- Schedule recurring runs for **continuous price surveillance**

## 依赖和前提条件

- APIFY_TOKEN
- process.env.APIFY_TOKEN
- ${process.env.APIFY_TOKEN

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
| SEC-02 数据外泄 | 🟡 警告 | 注意: https://api., fetch( |
| SEC-03 凭证获取 | 🟢 通过 | 未检测到凭证获取相关风险模式 |
| SEC-04 供应链风险 | 🟡 警告 | 注意: npm install |
| SEC-05 文件系统篡改 | 🟡 警告 | 注意: writefile |
| SEC-06 Prompt 注入 | 🟢 通过 | 未检测到Prompt 注入相关风险模式 |
| SEC-07 越权操作 | 🟢 通过 | 未检测到越权操作相关风险模式 |
| SEC-08 持久化机制 | 🟢 通过 | 未检测到持久化机制相关风险模式 |
| SEC-09 信息采集 | 🟡 警告 | 注意: id |
| SEC-10 混淆/反分析 | 🟢 通过 | 未检测到混淆/反分析相关风险模式 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 检测到 5 项警告: 命令执行, 数据外泄, 供应链风险, 文件系统篡改, 信息采集。无高危项。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-01 04:48 UTC
