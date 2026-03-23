# Taiwan Calendar Plugin

> Taiwan calendar query for accurate working day/holiday information. Use when user asks about Taiwan dates, working days, holidays, make-up workdays, or needs date calculations. Solves Claude's knowledge cutoff issues with Taiwan's administrative calendar.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Taiwan Calendar Plugin |
| **作者** | pigfoot |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/pigfoot-taiwan-calendar |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pigfoot/taiwan-calendar |
| **安全评级** | 🟢 Low |

## 功能概述
- Today's date and working day status
- Specific date queries (working day/holiday)
- Working day counts in date ranges
- N working days calculations
- Next working day/holiday lookups
- Today's date: Current Taiwan date (UTC+8) with weekday and working day status

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- macOS

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23