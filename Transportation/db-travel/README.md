# DB Travel

> "Plan journeys across Germany and Europe using the Deutsche Bahn API (v6.db.transport.rest). Covers ICE, IC, regional trains, S-Bahn, U-Bahn, trams, buses, ferries. Use when: (1) planning trips in Germany or cross-border European rail, (2) checking departure/arrival boards at German/European stations, (3) finding station IDs, (4) navigating cities like Berlin, Munich, Hamburg. Triggers on questions about German trains, DB, BVG, getting around Berlin, European rail connections."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | DB Travel |
| **作者** | mmichelli |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/mmichelli-db-travel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mmichelli/db-travel |
| **安全评级** | 🟢 Low |

## 功能概述
- Berlin Hbf: `8011160`
- München Hbf: `8000261`
- Hamburg Hbf: `8002549`
- Frankfurt (Main) Hbf: `8000105`
- Köln Hbf: `8000207`
- Flughafen BER: `8089110`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

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