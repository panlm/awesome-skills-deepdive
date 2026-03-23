# Astrai Inference Router

> Route all LLM calls through Astrai for 40%+ cost savings with intelligent routing and privacy controls

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Astrai Inference Router |
| **作者** | beee003 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/beee003-astrai-inference-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/beee003/astrai-inference-router |
| **安全评级** | 🟡 Medium |

## 功能概述
- Smart routing: Classifies each task (code, research, chat, creative) and picks the optimal model
- Cost savings: Bayesian learning finds the cheapest provider that meets your quality threshold
- Auto-failover: Circuit breaker switches providers when one goes down
- PII protection: Personally identifiable information stripped before reaching any provider
- EU routing: GDPR-compliant European-only routing with one setting
- Budget caps: Set daily spend limits to prevent runaway costs
- Real-time tracking: See exactly how much you're saving per request

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config.example.toml`
- `plugin.py`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23