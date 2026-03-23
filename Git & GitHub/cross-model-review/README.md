# Cross Model Review

> 使用两个不同 AI 模型进行对抗式方案审查，通过多轮迭代直到审查者批准或达到最大轮次

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cross Model Review |
| **作者** | don-gbot |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/don-gbot-cross-model-review |

## 功能概述
- 在两个不同 AI 模型（如 Anthropic + OpenAI）之间运行对抗式审查循环
- 审查者质疑方案，规划者修改方案，循环直到所有 CRITICAL 和 HIGH 问题解决
- 强制跨供应商审查，拒绝同供应商的自我审查
- 自动去重问题（Jaccard ≥ 0.6 检测重复）
- 为每个问题分配稳定 ID（ISS-001...），跟踪问题状态
- 使用 UNTRUSTED 分隔符包装方案内容，防止 Prompt 注入
- 最多 5 轮审查，超时后展示未解决问题供人工决定
- 生成最终审查摘要 JSON（含轮次数、发现问题数、解决数等）

## 使用场景
- 在实施复杂架构变更前，让不同 AI 模型交叉审查方案找出盲点
- 对重要的系统设计方案进行自动化的多轮质量把关
- 避免单一模型因共享相同推理风格而遗漏架构问题

## 依赖和前提条件
- Node.js >= 18.0.0
- OpenClaw（依赖 `sessions_spawn` 来调度审查者）
- 需要至少两个不同供应商的 AI 模型 API 凭证（如 OpenAI + Anthropic）
- 无需 npm install，零外部依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，4 项中风险。命令执行：发现直接命令执行指令；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
