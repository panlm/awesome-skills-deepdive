# KameleonDB

> Store and query structured data without planning schemas upfront. Use when you need to remember information, track entities across conversations, build knowledge bases, ingest API data, store user preferences, create CRM systems, or maintain any persistent state. Automatically evolves data structure as you discover new fields. No migrations, no schema design - just store data and query it.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | KameleonDB |
| **作者** | marcosnataqs |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/marcosnataqs-kameleondb |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/marcosnataqs/kameleondb |
| **安全评级** | 🟡 Medium |

## 功能概述
- Dynamic Schema Evolution - Add fields at runtime, zero lock operations
- Agent Hints Pattern - Queries return optimization suggestions inline
- Hybrid Storage - Flexible JSONB or dedicated typed tables
- Full Audit Trail - Every schema change tracked with reasoning
- JSON I/O - All operations support `--json` for machine-readable output

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `examples`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23