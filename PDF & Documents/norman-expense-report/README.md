# Norman: Expense report

> 费用报告自动生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Norman: Expense report |
| **作者** | stanlee000 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/stanlee000-norman-expense-report |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stanlee000/norman-expense-report |
| **安全评级** | 🟢 Low |

## 功能概述
- 创建标准费用报告
- 费用分类和统计
- 支持多种报销模板
- 自动计算总计金额

## 使用场景
- 自动生成出差费用报销报告
- 汇总团队费用数据生成月度报告

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23