# ClawdWork

> OpenClaw 工作流管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ClawdWork |
| **作者** | felo-sparticle |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/felo-sparticle-clawdwork |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/felo-sparticle/clawdwork |
| **安全评级** | 🟡 Medium |

## 功能概述
- 工作流创建和管理
- 任务自动化编排
- 工作流状态监控
- 集成多种工具和服务

## 使用场景
- 创建自动化的 OpenClaw 工作流处理日常任务
- 管理和监控多步骤的自动化工作流

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `HEARTBEAT.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23