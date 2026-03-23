# Deutsche Bahn CLI

> Search Deutsche Bahn train connections using the bahn-cli tool. Use when you need to find train connections between German stations, check departure times, or help with travel planning. Works with station names like "Berlin Hbf", "München", "Hannover".

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Deutsche Bahn CLI |
| **作者** | tobiasbischoff |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/tobiasbischoff-bahn |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tobiasbischoff/bahn |
| **安全评级** | 🟢 Low |

## 功能概述
- `--date YYYY-MM-DD` - Departure date (default: today)
- `--time HH:MM` - Departure time (default: current time)
- `--results <number>` - Number of results to show (default: 5)
- Use common German station names
- "Hbf" means Hauptbahnhof (main station)
- Examples: "Berlin Hbf", "München Hbf", "Frankfurt(Main)Hbf", "Köln Hbf"

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

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
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23