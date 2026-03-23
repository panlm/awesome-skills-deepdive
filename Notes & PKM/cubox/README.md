# Cubox Integration (International & China)

> Cubox 收藏夹集成 — 网页剪藏、标注和知识管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cubox Integration (International & China) |
| **作者** | liam8 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/liam8-cubox |
| **安全评级** | 🟡 Medium |

## 功能概述
- 网页内容剪藏和收藏
- 自动标注和高亮管理
- 智能分类和标签系统
- 全文搜索和知识检索

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Python 3.x 及相关依赖
- Cubox 账户
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23