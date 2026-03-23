# Quickbooks-Agent

> QuickBooks Online 集成 — 在线会计和财务管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Quickbooks-Agent |
| **作者** | paulbudveit |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/paulbudveit-quickbooks-online |
| **安全评级** | 🔴 High |

## 功能概述
- QuickBooks Online 账务管理
- 发票创建和客户管理
- 收支记录和银行对账
- 财务报表生成

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Docker
- Anki 桌面版 + AnkiConnect 插件
- QuickBooks Online 账户和 API 凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23