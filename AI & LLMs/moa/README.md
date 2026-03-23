# Mixture of Agents

> "Mixture of Agents: Make 3 frontier models argue, then synthesize their best insights into one superior answer. ~$0.03/query."

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
- OPENROUTER_API_KEY
- Complex analysis — due diligence, market research, technical evaluation
- Brainstorming — get diverse ideas, synthesize the best
- Fact-checking — cross-reference across models with different training data
- High-stakes decisions — when one model's blind spots could hurt you
- Contrarian thinking — different models have different biases

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `manifest.json`
- `scripts`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23