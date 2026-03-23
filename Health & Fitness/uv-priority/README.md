# Prioritize uv

> Prioritize uv over pip for all Python package management and execution. When running ANY Python command or CLI tool (python, dbt, pytest, etc.), MUST wrap with uv run.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Prioritize uv |
| **作者** | marcoracer |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/marcoracer-uv-priority |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/marcoracer/uv-priority |
| **安全评级** | 🟡 Medium |

## 功能概述
- Analyze code without importing project modules (linters, formatters, type checkers)
- Are one-off utilities not tied to your project
- Shouldn't pollute your project's dependencies
- Need to import your project modules
- Are part of your development workflow with project dependencies
- Run tests or your application

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。供应链风险：需要安装外部包且含管道安装；信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23