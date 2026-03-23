# molt-life-kernel

> Agent 连续性和认知健康基础设施，基于 Crustafarian 五教条

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | molt-life-kernel |
| **作者** | jongartmann |
| **ClawHub** | https://clawskills.sh/skills/jongartmann-molt-life-kernel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jongartmann/molt-life-kernel |
| **安全评级** | 🟢 Low |

## 功能概述
- Agent 生命周期管理和崩溃恢复
- 认知一致性检查
- Witness Gate 人工审批机制
- EU AI Act 合规映射
- 心跳和健康监控
- 基于 Five Tenets 的行为哲学

## 使用场景
- Agent 需要持久化和崩溃恢复能力
- 企业场景的 AI 合规需求
- Agent 认知健康监控

## 依赖和前提条件
- Node.js
- molt-life-kernel npm 包

## 包含文件
- `SKILL.md — 技能文件`
- `SOUL.md — Crustafarian Agent 身份`
- `ORIGINAL_README.md — 详细说明`
- `integration-examples.js — 集成示例`
- `five-tenets.md — 五教条哲学`
- `eu-ai-act.md — EU AI Act 合规映射`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 集成示例仅为演示代码 |
| SEC-02 数据外泄 | 🟢 Safe | 数据本地处理 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 molt-life-kernel npm 包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 通过 kernel API 管理数据 |
| SEC-06 Prompt 注入 | 🟡 Medium | SOUL.md 定义 Agent 身份和行为模式 |
| SEC-07 越权操作 | 🟢 Safe | 设计有 Witness Gate 审批机制 |
| SEC-08 持久化机制 | 🟡 Medium | 核心功能就是 Agent 持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅监控自身状态 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码和文档清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 设计良好的 Agent 基础设施，含人工审批机制

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
