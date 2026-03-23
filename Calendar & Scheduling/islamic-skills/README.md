# Islamic Companion

> Unified Islamic utilities for prayer times, fasting schedules, and Zakat calculations using a shared configuration.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Islamic Companion |
| **作者** | ilmimris |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/ilmimris-islamic-skills |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ilmimris/islamic-skills |
| **安全评级** | 🟡 Medium |

## 功能概述
- Prayer Times: Retrieve daily prayer times (Fajr, Dhuhr, Asr, Maghrib, Isha).
- Fasting: Check Imsak and Maghrib times for fasting.
- Zakat: Calculate Nisab thresholds for Gold and Silver based on current market prices.
- Quran: Search for verses by keyword or fetch specific Surah/Ayah with translation.
- Calendar: Generate a monthly prayer schedule for any city.
- Quotes: Fetch and display random Islamic quotes or setup daily automation.
- Scheduler: Generate OpenClaw cron commands to schedule daily prayer reminders.
- Caching: Minimizes API calls by caching daily results locally.

## 使用场景
- 管理日程和事件
- 自动化日历操作
- 跨平台日程同步

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `config.example.json`
- `lib`
- `requirements.txt`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23