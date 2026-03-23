# Agent Orchestration Multi Agent Optimize

> 多 Agent 系统优化工具包——协调分析、工作负载分配和成本感知编排

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Orchestration Multi Agent Optimize |
| **作者** | rustyorb |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/rustyorb-agent-orchestration-multi-agent-optimize |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rustyorb/agent-orchestration-multi-agent-optimize |
| **安全评级** | 🟡 Medium |

## 功能概述
- 多 Agent 协调优化：提升吞吐量和降低延迟
- 分布式性能分析：数据库、应用和前端三层 Agent 协同监控
- 瓶颈识别：通过 Agent 工作流分析找出协调障碍
- 成本效率追踪：感知预算约束，优化令牌和资源使用
- 提供 Python 代码示例的性能分析框架
- 支持渐进式编排变更和回归测试

## 使用场景
- 优化多 Agent 协作系统的整体性能和响应速度
- 在成本预算约束下最大化 Agent 系统的工作吞吐量
- 诊断复杂 Agent 工作流中的性能瓶颈并制定优化策略

## 依赖和前提条件
- Python 3.x

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
