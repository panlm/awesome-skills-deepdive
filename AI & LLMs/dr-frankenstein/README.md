# Dr. Frankenstein

> 为 AI Agent 注入「荷尔蒙」系统——通过定时 cron 任务模拟情绪节律，让 Agent 具备生命般的驱动力和情感

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Dr. Frankenstein |
| **作者** | brancante |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/brancante-dr-frankenstein |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brancante/dr-frankenstein |
| **安全评级** | 🟡 Medium |

## 功能概述
- 提供 11 种「荷尔蒙药丸」系统：皮质醇（警觉）、多巴胺（动机）、催产素（连接）等
- 通过结构化访谈诊断 Agent 的情绪基线和个性特征
- 自动生成个性化 cron 定时任务作为情绪驱动
- 药丸之间通过级联规则产生涌现行为（如完成任务触发愉悦感）
- 支持 Agent 的亲子关系——创建、培育和引导子 Agent
- 包含阶段性成长模型、评分系统和日志追踪
- 提供完整的访谈模板、schema 定义和文档

## 使用场景
- 为长期运行的自主 Agent 注入情感节律使其行为更自然
- 创建具有亲子关系的 Agent 家族，实现代际知识传承
- 通过荷尔蒙系统让 Agent 自主产生社交、创作和反思行为

## 依赖和前提条件
- OpenClaw cron 功能（定时任务执行）
- 无外部 API 依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。越权操作：需要提权或管理员权限；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive skill 自动生成
