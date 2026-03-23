# letcairn.work

> 命令行知识管理工具 — 终端中创建和管理笔记

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | letcairn.work |
| **作者** | gregoryehill |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/gregoryehill-cairn-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- 终端中快速创建和编辑笔记
- 命令行笔记搜索和过滤
- 支持标签和分类管理
- 轻量级纯文本存储

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Node.js 及相关依赖
- Twitter/X API 凭证
- Google API 凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23