# Job Execution Monitor

> 定时任务执行监控工具，在 cron 任务失败或错过调度时发出警报通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Job Execution Monitor |
| **作者** | tradmangh |
| **版本** | 1.0.3 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/tradmangh-job-execution-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tradmangh/job-execution-monitor |
| **安全评级** | 🔴 High |

## 功能概述
- 监控 cron 定时任务的执行状态
- 检测任务失败并立即发出告警
- 识别错过调度计划的任务
- 生成任务执行状态报告
- 支持多种告警通知渠道
- 记录任务执行历史日志

## 使用场景
- 运维团队监控关键 cron 任务确保按时执行
- 数据管道调度失败时及时收到告警
- 定期审查任务执行健康状况

## 依赖和前提条件
- 需要监控的 cron 任务配置
- 告警通知渠道配置
- OpenClaw 运行环境

## 包含文件
- `METADATA.json`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `config`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。凭证获取：需要多种敏感凭证；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
