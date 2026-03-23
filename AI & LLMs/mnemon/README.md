# Mnemon Memory

> LLM 智能体的持久化记忆 CLI 工具，支持事实存储、知识回溯和记忆生命周期管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mnemon Memory |
| **作者** | grivn |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/grivn-mnemon |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/grivn/mnemon |
| **安全评级** | 🟢 Low |

## 功能概述
- 为 AI 智能体提供持久化记忆存储能力
- 支持存储事实、回忆过往知识、关联相关记忆
- 完整的记忆生命周期管理（创建、更新、衰减、删除）
- 通过 Skill + Hook + Plugin 三层架构深度集成 OpenClaw
- Hook 在智能体启动时注入行为指南（agent:bootstrap）
- Plugin 提供提醒和推送功能
- 支持 Homebrew 和 Go install 两种安装方式

## 使用场景
- AI 智能体跨会话保持对用户偏好和历史交互的记忆
- 在长期项目中追踪和关联分散的知识片段
- 构建智能体的个人知识库，随时间积累并强化重要记忆

## 依赖和前提条件
- mnemon CLI（通过 brew install mnemon-dev/tap/mnemon 或 go install）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。命令执行：存在命令执行相关引用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
