# Evoagentx

> EvoAgentX 自进化 AI Agent 框架集成，支持从目标自动构建工作流并自我优化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Evoagentx |
| **作者** | nantes |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/nantes-evoagentx |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nantes/evoagentx |
| **安全评级** | 🟢 Low |

## 功能概述
- 集成 EvoAgentX 自进化 AI Agent 框架
- 支持从目标自动构建工作流
- 基于反馈的自我进化机制
- 多模型支持（OpenAI、Claude、DeepSeek、Qwen）
- 短期和长期记忆系统
- 人机协作回路（Human-in-the-loop）

## 使用场景
- 构建能够自我优化的复杂 AI 工作流
- 利用多种 LLM 模型进行任务分配和协作
- 在迭代反馈中持续改进 Agent 的任务执行能力

## 依赖和前提条件
- Python 3.12
- evoagentx（pip 安装）
- OpenAI API Key 或其他 LLM API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
