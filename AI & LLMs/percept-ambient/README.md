# Percept Ambient

> 环境智能模式，无需显式命令即可持续感知上下文，构建对话知识图谱

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Percept Ambient |
| **作者** | jarvis563 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/jarvis563-percept-ambient |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jarvis563/percept-ambient |
| **安全评级** | 🟢 Low |

## 功能概述
- 在后台持续运行，被动学习对话上下文
- 构建涵盖对话、实体和关系的知识图谱
- 自动追踪谈话对象、活跃项目和决策信息
- 支持基于感知的上下文查询（"你知道关于 XX 什么？"）
- 无需显式命令即可积累环境知识

## 使用场景
- 让 AI 智能体始终保持对工作环境的上下文感知
- 基于日常对话自动积累关于人物和项目的背景知识
- 快速回答关于特定人物或项目的上下文问题

## 依赖和前提条件
- percept CLI 工具
- 持续运行的后台进程

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive skill 自动生成
