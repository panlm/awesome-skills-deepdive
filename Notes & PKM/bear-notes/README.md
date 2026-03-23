# Bear Notes

> Bear 笔记应用集成 — 创建、搜索和管理 Bear 笔记

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bear Notes |
| **作者** | steipete |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/steipete-bear-notes |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建、编辑和搜索 Bear 笔记
- 标签管理和笔记分类
- 支持 Markdown 格式操作
- 跨设备笔记同步管理

## 使用场景
- 通过 AI Agent 快速创建和管理笔记内容
- 搜索和检索历史笔记信息
- 笔记自动分类、标注和整理

## 依赖和前提条件
- Bear 笔记应用 (macOS/iOS)

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23