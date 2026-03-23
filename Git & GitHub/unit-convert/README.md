# Unit Converter

> "Comprehensive unit converter for length, weight, temperature, area, volume, speed, time, and data. Use when: (1) converting between measurement units, (2) calculating unit equivalencies, (3) working with different measurement systems, or (4) any unit conversion needs. Supports metric, imperial, and digital units."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Unit Converter |
| **作者** | ouyangabel |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ouyangabel-unit-convert |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ouyangabel/unit-convert |
| **安全评级** | 🟢 Low |

## 功能概述
- Convert between metric and imperial units
- Calculate unit equivalencies
- Work with different measurement systems
- Convert digital storage sizes
- Metric: mm, cm, m, km
- Imperial: in, ft, yd, mi, inch, foot, yard, mile

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