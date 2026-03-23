# Hevy

> Query workout data from Hevy including workouts, routines, exercises, and history. Use when user asks about their workouts, gym sessions, exercise progress, or fitness routines.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hevy |
| **作者** | mjrussell |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/mjrussell-hevy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mjrussell/hevy |
| **安全评级** | 🟡 Medium |

## 功能概述
- Duplicate Prevention: `create-exercise` checks for existing exercises with the same name before creating. Use `--force` 
- API Limitations: Hevy API does NOT support deleting or editing exercise templates - only creating. Delete exercises manu
- API Rate Limits: Be mindful when fetching all data (--all flag)
- Weights: Defaults to lbs, use --kg for kilograms
- Pagination: Most commands auto-paginate, but limit flags help reduce API calls
- IDs: Workout/routine/exercise IDs are UUIDs, shown in detailed views

## 使用场景
- 记录和跟踪锻炼
- 制定训练计划
- 分析运动表现

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `pnpm-lock.yaml`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23