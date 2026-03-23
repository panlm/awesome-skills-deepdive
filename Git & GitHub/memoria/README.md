# Memoria

> AI 代理的结构化记忆系统，本地 Markdown 库 + Notion 双向同步。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Memoria |
| **作者** | kitakitsune0x |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/kitakitsune0x-memoria |

## 功能概述
- 初始化本地 Markdown 记忆库
- 存储多种类型的记忆：决策、经验教训、收件箱等
- 支持全文搜索和标签过滤
- 会话生命周期管理：wake → checkpoint → sleep
- 与 Notion 双向同步（推送/拉取/冲突处理）
- 本地优先设计，Markdown 文件作为数据源
- 支持干运行（dry-run）预览变更

## 使用场景
- 为 AI 代理建立持久化的结构化记忆系统，跨会话保持上下文
- 将 AI 代理的决策记录和经验教训同步到 Notion 便于团队查看
- 在多个环境间同步 AI 代理的记忆数据

## 依赖和前提条件
- Node.js 18+
- 安装方式：`npm install -g @kitakitsune/memoria`
- 可选：Notion Integration Token 和 Page ID（用于 Notion 同步）
- 运行 `memoria init` 初始化记忆库

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
