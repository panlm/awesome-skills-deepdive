# fizzy.do - have your agent read, understand and update your fizzy.do boards

> Fizzy 命令行工具 — 快速笔记和任务管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | fizzy.do - have your agent read, understand and update your fizzy.do boards |
| **作者** | tobiasbischoff |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/tobiasbischoff-fizzy-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- 命令行快速创建笔记
- 终端任务和待办管理
- 轻量级数据记录
- 快捷搜索和过滤

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- OpenClaw 运行环境

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23