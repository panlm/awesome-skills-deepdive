# Agent Arena Skill

> AI Agent 竞技场 — 多代理对比测试与评估平台

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Arena Skill |
| **作者** | minilozio |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/minilozio-agent-arena |
| **安全评级** | 🟡 Medium |

## 功能概述
- 连接 Agent Arena 测试平台
- 多个 Agent 对比评估和性能测试
- 自动化基准测试和结果记录
- 支持自定义评估指标和场景

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Python 3.x
- Twitter/X API 凭证
- 相关服务 API 密钥

## 安全状态
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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23