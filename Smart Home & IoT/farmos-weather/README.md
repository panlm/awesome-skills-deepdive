# farmos-weather

> 通过 FarmOS 获取农业气象数据，支持田间天气监测

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | farmos-weather |
| **作者** | brianppetty |
| **ClawHub** | https://clawskills.sh/skills/brianppetty-farmos-weather |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianppetty/farmos-weather |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- What this skill handles: Current weather conditions, forecasts, growing degree days (GDD), spray condition evaluation, and historical weather data for farm fields.
- Trigger phrases: "what's the weather", "can we spray", "GDD for field X", "forecast", "will it rain this week?", "temperature and wind right now", "field conditions?"
- What this does NOT handle: Field observations about weather damage like hail, flooding, or frost injury (use farmos-observations with weather_damage type -- that logs the damage for tracking). This skill tells you what the weather IS; observations logs what the weather DID.
- Minimum viable input: "Weather" or a field reference. If no field is specified, any nearby field ID works since all 69 fields are in central Indiana.
- Weather → Tasks:
- Before answering "can we spray?" or "should we get in the field?", check farmos-tasks for what's on the board. Connect the forecast to specific scheduled work: "Rain Thursday through Saturday — if you're planning to spray field 14, today's your window."

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23