# Entur Travel

> "Plan public transit trips in Norway using the Entur API. Covers all operators (Vy, Ruter, Kolumbus, etc.), all modes (bus, rail, tram, metro, ferry, coach). Use when: (1) planning a journey between places in Norway, (2) checking departure boards/next departures, (3) finding stop IDs or place names, (4) looking up real-time transit info. Triggers on questions about trains, buses, ferries, trams in Norway, getting to airports (Gardermoen, Torp, Flesland), or how do I get to X."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Entur Travel |
| **作者** | mmichelli |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/mmichelli-entur-travel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mmichelli/entur-travel |
| **安全评级** | 🟢 Low |

## 功能概述
- Oslo S: `NSR:StopPlace:59872`
- Oslo lufthavn (Gardermoen): `NSR:StopPlace:269`
- Bergen stasjon: `NSR:StopPlace:585`
- Trondheim S: `NSR:StopPlace:41742`
- Show times in local format (HH:MM), not ISO
- Summarize legs concisely: "🚆 RE11 Porsgrunn → Torp (10:17–10:50, platform 1)"

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
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23