# n8n-workflow-automation

> 设计带重试、日志和人工审查队列的 n8n 工作流 JSON

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | n8n-workflow-automation |
| **作者** | kowl64 |
| **ClawHub** | https://clawskills.sh/skills/kowl64-n8n-workflow-automation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kowl64/n8n-workflow-automation |
| **安全评级** | 🟢 Low |

## 功能概述
- 设计带健壮触发器的 n8n 工作流 JSON
- 幂等性设计（去重键防止重复）
- 错误处理和重试回退
- 人工审查队列（HITL）
- 审计日志和可观测性
- "无静默失败"门控机制
- 默认只读，显式请求才输出 JSON

## 使用场景
- 设计具有企业级错误处理的 n8n 工作流
- 创建带审计日志和人工审批的自动化流程

## 依赖和前提条件
- n8n 实例（用于导入生成的 JSON）

## 包含文件
- `SKILL.md` — 技能定义和工作流设计指南
- `assets/runbook-template.md` — 运行手册模板

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯设计指导，不执行命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅生成 JSON，不传输数据 |
| SEC-03 凭证获取 | 🟢 Safe | 明确要求通过环境变量引用凭证，不内嵌 |
| SEC-04 供应链风险 | 🟢 Safe | 纯文本，无依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 明确要求最小权限原则 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯文本指南 |

**综合评级: 🟢 Low**
**风险摘要:** 纯设计指导型 skill，安全实践良好（最小权限、凭证引用、审计日志）

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
