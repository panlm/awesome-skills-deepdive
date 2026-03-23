# Stock Market Intelligence

> Market data API for AI agents. Equities, fixed income, crypto, and macro. Bitcoin Lightning micropayments.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Stock Market Intelligence |
| **作者** | traderhc123 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/traderhc123-agenthc-market-intelligence |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/traderhc123/agenthc-market-intelligence |
| **安全评级** | 🟡 Medium |

## 功能概述
- Market data across equities, fixed income, crypto, and macro
- Agent-optimized format with direction, confidence, and urgency signals
- Compact format for reduced token usage in LLM context windows
- Batch queries to pull multiple datasets in one request
- Webhook alerts for key market events
- L402 micropayments via Bitcoin Lightning Network

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23