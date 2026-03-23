# Neuroboost Elixir

> 神经增强药剂 — 提升 Agent 认知和推理能力

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Neuroboost Elixir |
| **作者** | weidadong2359 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/weidadong2359-neuroboost-elixir |
| **安全评级** | 🟡 Medium |

## 功能概述
- 增强 Agent 认知处理能力
- 推理链优化和加速
- 注意力机制增强
- 知识关联强化

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Node.js 及相关依赖
- Anthropic API 密钥
- Craft 文档应用
- Twitter/X API 凭证
- Threads API 凭证
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。凭证获取：需要多种敏感凭证；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23