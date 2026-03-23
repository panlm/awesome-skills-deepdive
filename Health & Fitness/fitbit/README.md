# Fitbit

> Query Fitbit health data including sleep, heart rate, activity, SpO2, and breathing rate. Use when user asks about their fitness, sleep quality, steps, or health metrics.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Fitbit |
| **作者** | mjrussell |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/mjrussell-fitbit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mjrussell/fitbit |
| **安全评级** | 🟢 Low |

## 功能概述
- No parameter: today
- Specific date: `2026-01-05`
- Date range: `2026-01-01,2026-01-05`
- Relative: `yesterday`, `last-week`, `last-month`
- Custom relative: `last-2-days`, `last-3-weeks`, `last-2-months`
- Read-only access to Fitbit data

## 使用场景
- 同步和分析运动数据
- 追踪健康指标趋势
- 生成健身报告和洞察

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23