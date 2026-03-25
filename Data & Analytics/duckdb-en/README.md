# DuckDB CLI (DuckDB 命令行数据分析)

> DuckDB CLI 数据分析专家，支持 SQL 查询、数据处理和文件转换

## 📖 描述

DuckDB CLI Specialist 是一个用于数据分析、SQL 查询和文件格式转换的 skill。通过 DuckDB 命令行工具，直接对 CSV、Parquet 和 JSON 文件执行 SQL 查询，无需数据库服务器。

## ✨ 功能特点

- 直接对 CSV/Parquet/JSON 文件执行 SQL 查询
- 多种输出格式（CSV、JSON、Markdown 表格等）
- 文件格式互相转换
- 支持 glob 模式匹配多文件
- 与 shell 管道和脚本集成
- 无需启动数据库服务器即可分析数据

## 🚀 使用方法

### 安装
```bash
clawhub install camelsprout/duckdb-cli-ai-skills
```

### 前置要求
- 本地安装 DuckDB CLI

### 快速入门
```bash
# 查询 CSV 文件
duckdb -c "SELECT * FROM 'data.csv' LIMIT 10"

# 查询 Parquet 文件
duckdb -c "SELECT * FROM 'data.parquet'"

# Glob 多文件查询
duckdb -c "SELECT * FROM read_parquet('logs/*.parquet')"

# JSON 查询
duckdb -c "SELECT * FROM read_json_auto('data.json')"
```

### 使用场景
- 按条件筛选 CSV 文件记录
- 将 Parquet 导出转为 CSV
- 跨多个日志文件聚合统计
- 连接不同格式的数据文件
- 快速预览大型数据集

## 🔒 安全评估

| 项目 | 状态 |
|------|------|
| ClawHub 页面 | [查看](https://clawskills.sh/skills/camelsprout-duckdb-cli-ai-skills) |
| GitHub 源码 | [查看](https://github.com/openclaw/skills/tree/main/skills/camelsprout/duckdb-cli-ai-skills) |
| 安全状态 | ⚠️ 待验证 (Suspicious) |

## 📚 附加资源

- [ClawSkills 页面](https://clawskills.sh/skills/camelsprout-duckdb-cli-ai-skills)
- [GitHub 源码仓库](https://github.com/openclaw/skills/tree/main/skills/camelsprout/duckdb-cli-ai-skills)
- [DuckDB 官方文档](https://duckdb.org/docs/)
- 作者: @camelsprout
