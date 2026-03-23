# Wolfram Alpha

> Perform complex mathematical calculations, physics simulations, data analysis, and scientific queries via the Wolfram|Alpha LLM API. Use this skill when you need exact answers to quantitative questions.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Wolfram Alpha |
| **作者** | robert-janssen |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/robert-janssen-wolfram-alpha |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/robert-janssen/wolfram-alpha |
| **安全评级** | 🟢 Low |

## 功能概述
- Mathematics: Calculus, algebra, statistics.
- Science: Physics, chemistry, astronomy.
- Data: Economic data, geographic facts, demographics.
- Units: Unit conversions and currency exchange.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `wolfram_query.py`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。文件系统篡改：存在文件系统操作；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23