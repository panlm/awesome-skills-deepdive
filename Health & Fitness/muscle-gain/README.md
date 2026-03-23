# Muscle Gain

> Track muscle building with weight progression, protein tracking, and strength milestones

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Muscle Gain |
| **作者** | jhillin8 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/jhillin8-muscle-gain |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jhillin8/muscle-gain |
| **安全评级** | 🟢 Low |

## 功能概述
- "bulking progress"
- "strength gains"
- "protein today"
- Body weight - Daily logged weight
- Measurements - Arms, chest, shoulders, waist, thighs, neck (weekly)
- Strength lifts - Squat, deadlift, bench press, overhead press, barbell rows (log reps × weight)

## 使用场景
- 记录和跟踪锻炼
- 制定训练计划
- 分析运动表现

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