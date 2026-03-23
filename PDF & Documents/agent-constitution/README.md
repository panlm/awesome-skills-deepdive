# AgentConstitution

> 为 AI Agent 定义行为边界和安全策略的宪法框架

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AgentConstitution |
| **作者** | ztsalexey |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ztsalexey-agent-constitution |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ztsalexey/agent-constitution |
| **安全评级** | 🟡 Medium |

## 功能概述
- 定义 Agent 的行为规则和限制
- 建立安全策略和合规框架
- 支持自定义治理规则模板
- 提供 Agent 行为审计机制

## 使用场景
- 为企业 AI Agent 部署制定安全行为准则
- 建立 Agent 自治的治理框架

## 依赖和前提条件
- GitHub API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `check-compliance.txt`
- `check-emergency.txt`
- `get-rules.txt`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23