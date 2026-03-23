# Garmin Health Analysis

> Talk to your Garmin data naturally - "what was my fastest speed snowboarding?", "how did I sleep last night?", "what was my heart rate at 3pm?". Access 20+ metrics (sleep stages, Body Battery, HRV, VO2 max, training readiness, body composition, SPO2), download FIT/GPX files for route analysis, query elevation/pace at any point, and generate interactive health dashboards. From casual "show me this week's workouts" to deep "analyze my recovery vs training load".

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Garmin Health Analysis |
| **作者** | eversonl |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/eversonl-garmin-health-analysis |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eversonl/garmin-health-analysis |
| **安全评级** | 🟡 Medium |

## 功能概述
- Natural language queries: "How's my recovery this week?" → instant Body Battery analysis
- Sleep analysis: Hours, stages (light/deep/REM), quality scores, trends
- Recovery tracking: Body Battery, HRV, training readiness, stress levels
- Workout data: Activities by type, calories, duration, pace, elevation
- Health metrics: Resting heart rate, VO2 max, body composition, SPO2
- Activity files: Download FIT/GPX for detailed route and performance analysis

## 使用场景
- 同步和分析运动数据
- 追踪健康指标趋势
- 生成健身报告和洞察

## 依赖和前提条件
- Node.js / npm
- Python / pip
- OAuth

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `config.example.json`
- `install.sh`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23