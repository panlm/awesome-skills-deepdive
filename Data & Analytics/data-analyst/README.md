# data-analyst

> 数据可视化、报告生成、SQL 查询和电子表格自动化分析工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | data-analyst |
| **作者** | oyi77 |
| **ClawHub** | https://clawskills.sh/skills/oyi77-data-analyst |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/oyi77/data-analyst |
| **安全评级** | 🟡 Medium |

## 功能概述
- 执行 SQL 查询（支持 SQLite、PostgreSQL、MySQL）
- 分析电子表格数据（CSV、Excel、Google Sheets）
- 创建数据可视化图表和仪表盘
- 自动生成分析报告
- 数据清洗（缺失值、异常值处理）
- 描述性统计和趋势分析

## 使用场景
- 数据库快速查询和探索
- 业务数据分析和报告生成
- 数据质量检查和清洗

## 依赖和前提条件
- 数据库连接（SQLite/PostgreSQL/MySQL）
- DB_TYPE 和 DB_CONNECTION 环境变量

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含 SQL 模板和分析方法 |
| scripts/data-init.sh | 工作区初始化脚本 |
| scripts/query.sh | SQL 查询执行辅助脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 SQL 查询和数据库命令（psql/mysql/sqlite3），用户输入作为查询 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地操作，结果存为本地文件 |
| SEC-03 凭证获取 | 🟡 Medium | 从环境变量读取数据库连接字符串 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用系统数据库客户端 |
| SEC-05 文件系统篡改 | 🟢 Safe | 在指定工作区目录创建报告文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟡 Medium | SQL 查询权限取决于数据库连接配置 |
| SEC-08 持久化机制 | 🟢 Safe | 仅创建工作区目录结构 |
| SEC-09 信息采集 | 🟢 Safe | 仅查询用户指定的数据库 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 执行用户提供的 SQL 查询，权限取决于数据库连接配置

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
