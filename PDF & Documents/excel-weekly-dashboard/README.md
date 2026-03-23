# Excel weekly dashboards at scale

> 自动生成 Excel 周报数据看板

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Excel weekly dashboards at scale |
| **作者** | kowl64 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/kowl64-excel-weekly-dashboard |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kowl64/excel-weekly-dashboard |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动创建周报格式的 Excel 文件
- 数据可视化图表和仪表盘
- 支持自定义数据指标
- 模板化报告生成

## 使用场景
- 每周自动生成团队工作数据报表
- 创建项目进度的可视化周报看板

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `assets`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。文件系统篡改：存在文件系统操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23