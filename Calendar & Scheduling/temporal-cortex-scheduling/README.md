# temporal-cortex-scheduling

> 时间皮层调度模块 — 智能任务排程和优化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | temporal-cortex-scheduling |
| **作者** | billylui |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/billylui-temporal-cortex-scheduling |
| **安全评级** | 🔴 High |

## 功能概述
- 智能任务排程和优化
- 资源约束调度算法
- 优先级驱动的任务编排
- 调度冲突自动解决

## 使用场景
- 日常事务调度和时间管理自动化
- 工作流程编排和任务协调
- 与其他 OpenClaw 技能配合构建自动化流程

## 依赖和前提条件
- Node.js
- Docker
- CalDAV 日历服务器
- Fastmail 账户和 API 凭证
- Google Calendar API 凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23