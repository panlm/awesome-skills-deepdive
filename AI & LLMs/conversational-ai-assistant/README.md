# Conversational Ai Assistant

> Natural language interface for querying Greek accounting data. Ask questions in English, get answers from across all system skills.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Conversational Ai Assistant |
| **作者** | satoshistackalotto |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-conversational-ai-assistant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/conversational-ai-assistant |
| **安全评级** | 🔴 High |

## 功能概述
- English In, English Out: Every interaction is in English. Greek data — names, addresses, regulatory terms, AFM numbers —
- Read First, Act Second: The vast majority of interactions are queries. The assistant surfaces information freely. Action
- Honest About Uncertainty: When data is incomplete, when a calculation has low confidence, or when a question requires pr
- Skill Orchestration, Not Duplication: The assistant does not reimplement any skill logic. It calls the appropriate skill
- Context Awareness: Within a conversation session, the assistant remembers what has been discussed. If an assistant asks 
- Professional Tone: Responses are clear, concise, and professional — appropriate for an accounting firm environment. No u

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `EVALS.json`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23