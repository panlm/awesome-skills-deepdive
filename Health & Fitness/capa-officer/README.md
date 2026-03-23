# Capa Officer

> CAPA system management for medical device QMS. Covers root cause analysis, corrective action planning, effectiveness verification, and CAPA metrics. Use for CAPA investigations, 5-Why analysis, fishbone diagrams, root cause determination, corrective action tracking, effectiveness verification, or CAPA program optimization.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Capa Officer |
| **作者** | alirezarezvani |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-capa-officer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/capa-officer |
| **安全评级** | 🟢 Low |

## 功能概述
- CAPA investigation
- root cause analysis
- 5 Why analysis
- fishbone diagram
- corrective action
- preventive action

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23