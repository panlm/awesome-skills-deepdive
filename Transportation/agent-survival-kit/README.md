# Agent Survival Kit

> AI Agent 生存工具包，提供 Agent 在复杂环境中运行所需的基础工具集

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Survival Kit |
| **作者** | gpunter |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/gpunter-agent-survival-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gpunter/agent-survival-kit |
| **安全评级** | 🟢 Low |

## 功能概述
- 提供 Agent 运行时所需的基础工具和配置
- 环境检测和自动适配功能
- 错误恢复和重试机制
- 日志记录和状态监控

## 使用场景
- 新部署的 Agent 快速获取运行所需的基础环境配置
- Agent 在不稳定网络环境中保持运行稳定性

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

> 本文档由 awesome-skills-deepdive skill 自动生成
