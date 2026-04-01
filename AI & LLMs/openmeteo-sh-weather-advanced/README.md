# openmeteo-sh-weather-advanced

> Advanced weather from free OpenMeteo API: historical data, detailed variable selection, model choice, past-days, and in-depth forecasts. Use when the user asks about historical weather, specific weather models, niche variables (pressure, dew point, snow depth, etc.), or needs fine-grained control beyond simple current/forecast queries.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | openmeteo-sh-weather-advanced |
| **作者** | lstpsche |
| **ClawHub** | https://clawskills.sh/skills/lstpsche-openmeteo-sh-weather-advanced |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lstpsche/openmeteo-sh-weather-advanced |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- `--city=NAME` — city name, auto-geocoded; usually sufficient on its own
- `--country=CODE` — optional country hint to disambiguate (e.g. US, GB). Only needed when city name is ambiguous. Pass whatever you have or omit.
- `--lat=NUM --lon=NUM` — direct WGS84 coordinates, skips geocoding
- `--current` — fetch current conditions
- `--forecast-days=N` — days of forecast, 0–16 (default 7)
- `--forecast-since=N` — start from day N of the forecast (1=today, 2=tomorrow, etc.). Trims the window server-side. Must be <= forecast-days.

## 依赖和前提条件

- 无特殊依赖

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
