# csv-pipeline

> 处理、转换、分析和生成 CSV/JSON 表格数据报告

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | csv-pipeline |
| **作者** | gitgoodordietrying |
| **ClawHub** | https://clawskills.sh/skills/gitgoodordietrying-csv-pipeline |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/csv-pipeline |
| **安全评级** | 🟢 Low |

## 功能概述
- 支持 CSV、TSV、JSON、JSON Lines 格式处理
- 数据筛选、排序、去重
- 数据集合并和聚合计算
- 格式转换（CSV↔JSON 互转）
- 使用标准 CLI 工具（awk/sort/cut）快速操作
- Python 复杂数据转换

## 使用场景
- 分析和清洗业务数据文件
- 多数据源合并和 ETL 处理
- 生成汇总统计报告

## 依赖和前提条件
- Python 3 或 uv

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含各种数据处理模板 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用标准 CLI 工具（awk/sort/python），参数来自用户 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地数据处理 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用 Python 标准库 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅处理用户指定的数据文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯本地数据处理工具，使用标准库，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
