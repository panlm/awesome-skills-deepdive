# Shipp enables a faster way to create connections to real-time data. It's cost-effective, fast to run, and easy to start.

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Shipp enables a faster way to create connections to real-time data. It's cost-effective, fast to run, and easy to start. |
| **作者** | kclonts |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/kclonts-shipp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kclonts/shipp |
| **安全评级** | 🟡 Medium |

## 功能概述
- Authentication — Multiple methods supported (Bearer token, query parameter, headers)
- Connections — Create reusable live-data queries with natural-language `filter_instructions`
- Running Connections — Poll for real-time events with cursor-based pagination
- Schedule — Discover upcoming and recent games by sport
- Data Shape — Schema-flexible `data[]` responses and how to handle them defensively
- Error Handling — Status codes, hints, and retry strategies

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23