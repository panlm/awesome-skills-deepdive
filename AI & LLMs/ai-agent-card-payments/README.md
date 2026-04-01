# Ai Agent Card Payments

> 为 AI 代理提供虚拟卡支付能力，支持策略控制和审批流程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai Agent Card Payments |
| **作者** | proxyhq |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/proxyhq-ai-agent-card-payments |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/proxyhq/ai-agent-card-payments |
| **安全评级** | 🟡 Medium |

## 功能概述
- 创建支付意图并自动签发虚拟卡
- 通过策略引擎（Proxy）强制执行消费限额和规则
- 高额消费触发人工审批流程
- 支持交易证据和收据附件用于审计追踪
- 提供 KYC 状态查询和余额检查
- 通过 MCP 协议集成支付 API

## 使用场景
- 让 AI 代理在设定限额内自主完成采购任务
- 为代理的每笔消费提供审计追踪和合规记录
- 实现高额消费自动触发人工审批的安全支付流程

## 依赖和前提条件
- Proxy 平台账号及 Agent Token
- MCP 服务器配置（mcp.useproxy.ai）
- KYC 验证完成

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
