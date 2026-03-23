# Mixture of Agents

> 混合智能体架构：让 3 个前沿 AI 模型互相辩论，综合最佳洞察生成优质回答，每次约 $0.03

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mixture of Agents |
| **作者** | jscianna |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/jscianna-moa |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jscianna/moa |
| **安全评级** | 🟡 Medium |

## 功能概述
- 让 3 个不同的前沿 AI 模型对同一问题进行辩论
- 综合各模型的最佳洞察，生成优于任何单一模型的回答
- 支持独立 CLI（Node.js）和 OpenClaw Skill 两种使用模式
- 每次查询成本约 $0.03，性价比极高
- 特别适合需要多角度分析的复杂问题
- 通过 OpenRouter 调用多个模型 API

## 使用场景
- 复杂分析任务：尽职调查、市场研究、技术评估
- 头脑风暴：获取多元化创意并综合最佳方案
- 事实核查：通过多模型交叉验证提高准确性

## 依赖和前提条件
- OPENROUTER_API_KEY 环境变量
- Node.js 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
