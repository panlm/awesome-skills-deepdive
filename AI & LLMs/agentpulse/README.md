# AgentPulse

> 追踪 AI 代理的 LLM API 费用、Token 用量、延迟和错误

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AgentPulse |
| **作者** | sru4ka |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/sru4ka-agentpulse |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sru4ka/agentpulse |
| **安全评级** | 🟡 Medium |

## 功能概述
- 实时追踪每次 LLM API 调用的费用和 Token 消耗
- 监控 API 响应延迟和错误率
- 提供 Web 仪表盘（agentpulse.dev）可视化展示数据
- 通过简单的 curl 命令上报事件数据
- 支持按代理名称和框架分类追踪
- 检测速率限制和异常调用模式

## 使用场景
- 监控 AI 代理的日常 API 消费，及时发现费用异常
- 分析代理的 API 调用模式，优化 Token 使用效率
- 在出现速率限制或 API 错误时快速定位问题

## 依赖和前提条件
- AgentPulse 账号及 API Key（从 agentpulse.dev 获取，前缀 `ap_`）
- 环境变量 `AGENTPULSE_API_KEY`
- curl 命令行工具

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
