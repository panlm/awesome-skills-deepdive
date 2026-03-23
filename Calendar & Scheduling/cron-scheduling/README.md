# Cron & Scheduling

> Cron 调度工具 — 创建和管理定时任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cron & Scheduling |
| **作者** | gitgoodordietrying |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/gitgoodordietrying-cron-scheduling |
| **安全评级** | 🔴 High |

## 功能概述
- 创建和管理 Cron 定时任务
- 灵活的调度表达式支持
- 任务执行日志和监控
- 失败重试和告警机制

## 使用场景
- 自动化定时任务的创建和管理
- 周期性工作流编排和执行监控
- 任务调度优化和故障恢复

## 依赖和前提条件
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。越权操作：需要提权或管理员权限；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23