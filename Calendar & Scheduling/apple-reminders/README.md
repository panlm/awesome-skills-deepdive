# Apple Reminders

> macOS 提醒事项集成 — 创建和管理 Apple Reminders 任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apple Reminders |
| **作者** | steipete |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/steipete-apple-reminders |
| **安全评级** | 🟢 Low |

## 功能概述
- 创建和管理 Apple 提醒事项
- 设置截止日期和优先级
- 按列表分类管理待办
- 已完成任务标记和归档

## 使用场景
- 语音或文字快速创建提醒和待办事项
- 基于对话上下文自动生成相关任务
- 待办完成追踪和逾期提醒

## 依赖和前提条件
- Node.js 及相关依赖
- macOS 系统 + 提醒事项应用

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23