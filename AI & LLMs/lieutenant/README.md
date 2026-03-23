# Lieutenant - AI Agent Security

> "AI agent security and trust verification. Scan messages, agent cards, and A2A communications for prompt injection, jailbreaks, and malicious patterns. Use when protecting agents from attacks, verifying external agents, or scanning untrusted content."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lieutenant - AI Agent Security |
| **作者** | jd-delatorre |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/jd-delatorre-lieutenant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jd-delatorre/lieutenant |
| **安全评级** | 🔴 High |

## 功能概述
- 65+ threat patterns across 10 categories
- Semantic analysis catches paraphrased attacks (requires OpenAI API key)
- A2A integration for agent-to-agent communication protection
- TrustAgents API for reputation data and crowdsourced threat intel

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23