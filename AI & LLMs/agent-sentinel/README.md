# AgentSentinel Safety Layer

> Agent 运行安全熔断器——强制执行预算限制和敏感操作审批

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AgentSentinel Safety Layer |
| **作者** | jimmystacks |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/jimmystacks-agent-sentinel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jimmystacks/agent-sentinel |
| **安全评级** | 🟡 Medium |

## 功能概述
- 预算控制：为 Agent 设定财务预算上限，超限自动熔断
- 预检机制：执行复杂任务前强制检查剩余预算
- 敏感操作拦截：删除文件、数据传输、执行未知代码等操作需预先审批
- 人工审批工作流：当操作被标记为 APPROVAL_REQUIRED 时触发人工确认
- 实时监控仪表盘：通过 agentsentinel.dev 查看 Agent 运行状态
- 支持云端同步：登录后可远程监控和管理 Agent

## 使用场景
- 为自主运行的 Agent 设置成本上限防止意外高额消费
- 在 Agent 执行破坏性操作前强制要求人工审批
- 监控多个 Agent 的实时运行状态和资源消耗

## 依赖和前提条件
- Python 3.x
- agentsentinel-sdk[remote]（pip 安装）
- AGENT_SENTINEL_API_KEY 环境变量（可选，用于云端同步）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 6 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
