# duckdb-cli-ai-skills

> DuckDB CLI 专家技能，用于 SQL 分析和数据处理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | duckdb-en |
| **作者** | camelsprout |
| **ClawHub** | https://clawskills.sh/skills/camelsprout-duckdb-cli-ai-skills |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/camelsprout/duckdb-cli-ai-skills |
| **安全评级** | 🟢 Low |

## 功能概述
- DuckDB CLI 完整操作指南
- 直接用 SQL 查询 CSV、Parquet、JSON 文件
- 数据格式转换（CSV↔Parquet↔JSON）
- 支持 18 种输出格式
- 数据库操作和分析
- 安全模式（限制文件访问）

## 使用场景
- 本地文件快速 SQL 分析
- 数据格式转换（如 CSV 转 Parquet）
- 大规模数据分析（不需要传统数据库）

## 依赖和前提条件
- DuckDB CLI

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，DuckDB 完整文档 |
| ORIGINAL_README.md | 原始说明 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，仅提供 DuckDB 使用指南 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地操作 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 DuckDB |
| SEC-05 文件系统篡改 | 🟢 Safe | 在 DuckDB 安全模式下受限 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯知识型 skill，提供 DuckDB CLI 使用指南，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
