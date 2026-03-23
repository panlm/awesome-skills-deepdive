# Weather via OpenMeteo (via openmeteo-sh cli; advanced ver)

> "Advanced weather from free OpenMeteo API: historical data, detailed variable selection, model choice, past-days, and in-depth forecasts. Use when the user asks about historical weather, specific weather models, niche variables (pressure, dew point, snow depth, etc.), or needs fine-grained control beyond simple current/forecast queries."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Weather via OpenMeteo (via openmeteo-sh cli; advanced ver) |
| **作者** | lstpsche |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/lstpsche-openmeteo-sh-weather-advanced |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lstpsche/openmeteo-sh-weather-advanced |
| **安全评级** | 🔴 High |

## 功能概述
- `--llm` output format — compact TSV designed for AI agents, reduces token usage by ~90% compared to key=value formats
- City name resolution — `--city=London` instead of lat/lon coordinates
- Weather code resolution — WMO codes are automatically converted to text (e.g. "Light rain" instead of code 61)
- Built-in variable help — `openmeteo weather help --daily-params` lists all available variables with descriptions
- Historical data — reanalysis data from 1940 via ERA5, CERRA, ECMWF IFS
- No API key required — uses the free Open-Meteo API

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- macOS
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23