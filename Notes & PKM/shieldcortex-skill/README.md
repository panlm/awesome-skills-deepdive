# Shieldcortex Skill

> ShieldCortex 安全防护 — Agent 安全监控和防御系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Shieldcortex Skill |
| **作者** | jarvis-drakon |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/jarvis-drakon-shieldcortex-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- Agent 安全行为监控
- 异常操作检测和告警
- 安全策略执行和审计
- 威胁情报整合和响应

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Node.js 及相关依赖
- Bear 笔记应用 (macOS/iOS)
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23