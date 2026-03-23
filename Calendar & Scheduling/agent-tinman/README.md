# Tinman -  AI Failure Mode Research, Prompt Injection & Tool Exfil Detection

> Agent 铁皮人 — 自动化任务执行和智能调度

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Tinman -  AI Failure Mode Research, Prompt Injection & Tool Exfil Detection |
| **作者** | oliveskin |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/oliveskin-agent-tinman |
| **安全评级** | 🔴 High |

## 功能概述
- 自动化任务执行引擎
- 智能任务调度和编排
- 任务依赖管理
- 执行结果追踪和报告

## 使用场景
- 日常事务调度和时间管理自动化
- 工作流程编排和任务协调
- 与其他 OpenClaw 技能配合构建自动化流程

## 依赖和前提条件
- Python 3.x
- Node.js 及相关依赖
- Medium 账户
- Twitter/X API 凭证
- Fabric 框架
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，6 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23