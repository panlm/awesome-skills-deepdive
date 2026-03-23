# Calorie Counter

> Track daily calorie and protein intake, set goals, and log weight. Use when user mentions food they ate, wants to know remaining calories, or needs to track weight. Stores data in SQLite with automatic daily totals.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Calorie Counter |
| **作者** | cnqso |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/cnqso-calorie-counter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cnqso/calorie-counter |
| **安全评级** | 🟢 Low |

## 功能概述
- Manual calorie entry - No unreliable nutrition APIs
- Protein tracking - Monitor daily protein intake
- Weight logging - Track weight in pounds
- Instant feedback - See totals immediately after adding food
- SQLite database - Reliable, local storage
- History & trends - View past days and progress

## 使用场景
- 跟踪饮食和营养摄入
- 搜索和管理食谱
- 制定健康饮食计划

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `ORIGINAL_README.md`
- `QUICK_START.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23