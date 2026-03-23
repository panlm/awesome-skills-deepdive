# Apple Mail

> macOS 邮件应用集成 — 读取、搜索和管理 Apple Mail 邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Apple Mail |
| **作者** | tyler6204 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/tyler6204-apple-mail |
| **安全评级** | 🟢 Low |

## 功能概述
- 读取和搜索 Apple Mail 邮件
- 按发件人、主题、日期过滤邮件
- 提取邮件内容和附件信息
- 支持多邮箱账户管理

## 使用场景
- 让 AI Agent 自动检查和汇总未读邮件
- 根据邮件内容自动创建任务和提醒
- 智能邮件分类和优先级排序

## 依赖和前提条件
- macOS 系统 + 邮件应用
- Gmail API 凭证
- Google API 凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23