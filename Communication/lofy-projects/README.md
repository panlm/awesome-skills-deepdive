# Lofy Projects

> Project management for the Lofy AI assistant — tracks multiple projects with milestones, priority scoring engine (urgency × job relevance × momentum × energy match), meeting prep automation, time logging, stale project alerts, and work session recommendations. Use when managing projects, prioritizing work, preparing for meetings, or tracking milestones and deadlines.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lofy Projects |
| **作者** | harrey401 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/harrey401-lofy-projects |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/harrey401/lofy-projects |
| **安全评级** | 🟢 Low |

## 功能概述
- < 30 min: Quick tasks — email, review, read, update docs
- 30-60 min: Medium — write one function, prep notes, apply to 1 job
- 1-2 hours: Focused — implement a feature, write paper section, debug
- 2+ hours: Deep work — major development sessions
- "Worked on [project] for 2 hours" → update time_log, last_updated
- "[Feature] is working now" → update milestone status

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23