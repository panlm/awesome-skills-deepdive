# Which LLM? Deterministic model selection for agents

> Deterministic decision-ranking API with HTTP 402 payments and outcome credits.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Which LLM? Deterministic model selection for agents |
| **作者** | zapkid |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/zapkid-which-llm |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zapkid/which-llm |
| **安全评级** | 🟡 Medium |

## 功能概述
- Sends requests to the Which‑LLM API
- Uses `POST /decision/optimize` to get a recommended model and fallback plan
- Uses `POST /decision/outcome` to report real execution results
- Explains the request and response shapes for the public API
- Describes how to retry requests after payment has been satisfied externally
- It does not call an LLM directly
- It does not execute arbitrary code from your prompt
- It does not require unrelated files or system access beyond API usage and payment handling

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `skill.json`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23