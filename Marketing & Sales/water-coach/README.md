# Water Coach

> "Hydration tracking and coaching skill. Use when user wants to track water intake, get reminders to drink water, log body metrics, or get analytics on hydration habits."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Water Coach |
| **作者** | oristides |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/oristides-water-coach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/oristides/water-coach |
| **安全评级** | 🟢 Low |

## 功能概述
- Reminder schedules after first setup (user already configured)
- "How much water did you drink?"
- Only weight/goal (first time)
- drank_at is MANDATORY - always required
- If user doesn't specify drank_at → assume drank_at = logged_at
- Cumulative is calculated at query time (not stored)

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip

## 包含文件
- `CHANGELOG.md`
- `SKILL.md`
- `_meta.json`
- `evaluation`
- `references`
- `scripts`
- `skills`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。命令执行：存在命令执行相关引用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23