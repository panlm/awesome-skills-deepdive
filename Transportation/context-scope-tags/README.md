# Context Scope Tags

> 上下文作用域标签，在多话题对话中通过显式标签防止主题混淆

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Context Scope Tags |
| **作者** | phenomenoner |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/phenomenoner-context-scope-tags |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/phenomenoner/context-scope-tags |
| **安全评级** | 🟢 Low |

## 功能概述
- 为对话内容添加显式作用域标签
- 防止多话题聊天中的上下文混淆
- 支持主题边界的自动检测
- 清晰管理并行对话流

## 使用场景
- 在同时讨论多个项目时保持每个话题的上下文隔离
- 切换对话主题时自动标记并隔离上下文

## 依赖和前提条件
- 无特殊依赖

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式

> 本文档由 awesome-skills-deepdive skill 自动生成
