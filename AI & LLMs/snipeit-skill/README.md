# snipeit-skill

> Interact with Snipe-IT asset management via REST API. Use when working with assets (hardware), users, licenses, accessories, consumables, components, locations, departments, models, manufacturers, status labels, categories, suppliers, maintenances, reports. Trigger on: "snipe", "asset", "hardware", 

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | snipeit-skill |
| **作者** | bivex |
| **ClawHub** | https://clawskills.sh/skills/bivex-snipeit-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bivex/snipeit-skill |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- SNIPEIT_URL        # e.g. https://assets.w-w.top
- SNIPEIT_API_TOKEN  # Bearer token from your profile → API keys
- Always send both `Content-Type: application/json` AND `Accept: application/json`
- API always returns `200 OK` — check `.status` field for `"success"` / `"error"`
- Use `?limit=` and `?offset=` for pagination (max 500 per request)
- Dates format: `YYYY-MM-DD`

## 依赖和前提条件

- Always send both `Content-Type: application/json` AND `Accept: application/json`
- API always returns `200 OK` — check `.status` field for `"success"` / `"error"`
- Use `?limit=` and `?offset=` for pagination (max 500 per request)
- Dates format: `YYYY-MM-DD`
- Monetary values: string `"99.99"` not number

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
