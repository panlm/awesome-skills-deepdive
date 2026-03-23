# Prioritize uv

> UV 紫外线指数监控工具

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
- If you see `uv run ruff check .` in the project, don't change to `uvx`
- If the user specified `uv run pytest`, maintain the pattern

## 使用场景
- 获取实时紫外线指数数据
- 基于 UV 指数提供防晒建议
- 跟踪紫外线暴露时间和安全阈值

## 依赖和前提条件
- Python / pip
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `skill.json`

## 安全状态
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
