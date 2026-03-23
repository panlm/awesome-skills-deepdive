# Create Dxf

> Create RFQ-ready 2D DXF (and optional SVG preview) files from a strict, validated JSON spec derived from a natural-language design prompt. Use for sheet/plate parts (waterjet/laser/router) like mounting plates, gussets, brackets, hole patterns, and slots.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Create Dxf |
| **作者** | ajmwagar |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ajmwagar-create-dxf |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ajmwagar/create-dxf |
| **安全评级** | 🟢 Low |

## 功能概述
- `out/<name>.dxf`
- `out/<name>.svg`
- DXF uses simple entities for compatibility: closed `LWPOLYLINE` outer profile + `CIRCLE` holes.
- Default layers are manufacturing-oriented:
- `CUT_OUTER` (outer perimeter)
- `CUT_INNER` (holes/slots)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
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