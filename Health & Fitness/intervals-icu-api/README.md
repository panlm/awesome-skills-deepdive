# Intervals Icu Api

> Complete guide for accessing and managing training data with the intervals.icu API. Use when working with Intervals.icu athlete profiles, activities, workouts, events, wellness data, and training plans. Covers authentication, retrieving activities with combined data fields, managing calendar events with planned workouts, and creating/updating training data. Includes curl examples for all major operations.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Intervals Icu Api |
| **作者** | pseuss |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/pseuss-intervals-icu-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pseuss/intervals-icu-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- Get Activities: Retrieve completed workouts with power, heart rate, and load data
- Manage Calendar: Create, update, and delete planned workouts on your training calendar
- Combine Data: Use field selectors to pull activities with contextual metrics (fitness, fatigue, zones)
- Log Wellness: Track sleep, soreness, resting HR, and recovery metrics
- Upload Data: Create manual activities and bulk-import training sessions
- Export Workouts: Download planned workouts in device formats (.zwo, .mrc, .erg, .fit)

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- API Key
- OAuth

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
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23