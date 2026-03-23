# Financial Calculator Pro

> Advanced financial calculator with future value tables, present value, discount calculations, markup pricing, and compound interest. Use when calculating investment growth, pricing strategies, loan values, discounts, or comparing financial scenarios across different rates and time periods. Includes both CLI and interactive web UI.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Financial Calculator Pro |
| **作者** | tarigha |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tarigha-financial-calculator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tarigha/financial-calculator |
| **安全评级** | 🟡 Medium |

## 功能概述
- 7 calculator types with intuitive tabs
- Real-time calculations
- Interactive tables
- Beautiful gradient UI
- Mobile-responsive design
- Investment growth projections

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `assets`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23