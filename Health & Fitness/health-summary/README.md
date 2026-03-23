# Health Summary

> Generate daily/weekly/monthly health summaries with nutrition totals, target comparisons, and trends.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Health Summary |
| **作者** | yusaku-0426 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/yusaku-0426-health-summary |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yusaku-0426/health-summary |
| **安全评级** | 🟢 Low |

## 功能概述
- `totals`: カロリー、P/C/F、食物繊維、糖質、ナトリウム、飽和脂肪、水分、運動時間
- `targets`: 目標値（config/health_targets.json から）
- `deltas`: 目標との差分
- `latest_weight`: 直近の体重
- `latest_sleep`: 直近の睡眠時間
- kcal: 2,200 / P: 165g / C: 275g / F: 55g

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm

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
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23