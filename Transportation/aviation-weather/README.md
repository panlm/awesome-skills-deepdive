# Aviation Weather

> Fetch aviation weather data (METAR, TAF, PIREPs) from aviationweather.gov. Use for flight planning, weather briefings, checking airport conditions, or any pilot-related weather queries. Triggers on "METAR", "TAF", "flight weather", "airport weather", "aviation weather", "pilot report", "PIREP", or specific ICAO codes.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Aviation Weather |
| **作者** | dimitryvin |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/dimitryvin-aviation-weather |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dimitryvin/aviation-weather |
| **安全评级** | 🟢 Low |

## 功能概述
- 🟢 VFR - Ceiling >3000ft AGL and visibility >5sm
- 🔵 MVFR - Ceiling 1000-3000ft or visibility 3-5sm
- 🔴 IFR - Ceiling 500-1000ft or visibility 1-3sm
- 🟣 LIFR - Ceiling <500ft or visibility <1sm
- `--metar`, `-m`: Fetch METAR (default)
- `--taf`, `-t`: Fetch TAF forecast

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23