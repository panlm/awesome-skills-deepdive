# Tweet Processor

> 推文处理器 — 抓取、分析和处理 Twitter/X 内容

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Tweet Processor |
| **作者** | caqlayan |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/caqlayan-tweet-processor |
| **安全评级** | 🟢 Low |

## 功能概述
- 抓取和解析 Twitter/X 推文
- 推文内容分析和情感识别
- 推文数据结构化处理
- 批量推文操作支持

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Twitter/X API 凭证

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23