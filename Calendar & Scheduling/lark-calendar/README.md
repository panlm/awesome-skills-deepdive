# Lark Calendar & Tasks

> Lark 日历集成 — 创建和管理 Lark 平台日程事件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lark Calendar & Tasks |
| **作者** | boyangwang |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/boyangwang-lark-calendar |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建和管理 Lark 平台日程事件
- 会议安排和参与者管理
- 日程同步和提醒设置
- Lark 日历 API 操作

## 使用场景
- 通过自然语言创建和管理日历事件
- 自动检测日程冲突并建议最佳时间
- 每日日程摘要和即将到来的事件提醒

## 依赖和前提条件
- Node.js
- 飞书应用凭证
- Lark 应用凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23