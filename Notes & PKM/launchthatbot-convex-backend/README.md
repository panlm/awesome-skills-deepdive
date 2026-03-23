# Launchthatbot Convex Backend

> Convex 后端集成 — 实时数据库和后端服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Launchthatbot Convex Backend |
| **作者** | launchthatbot |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/launchthatbot-launchthatbot-convex-backend |
| **安全评级** | 🔴 High |

## 功能概述
- Convex 实时数据库操作
- 后端函数调用和管理
- 数据订阅和实时更新
- 无服务器后端集成

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Node.js
- OpenAI API 密钥
- Twitter/X API 凭证
- Convex 后端服务
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 7 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23