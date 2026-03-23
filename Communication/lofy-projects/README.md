# Lofy Projects

> Lofy AI 助手的项目管理工具，支持多项目追踪、里程碑管理和任务分配

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lofy Projects |
| **作者** | harrey401 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/harrey401-lofy-projects |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/harrey401/lofy-projects |
| **安全评级** | 🟢 Low |

## 功能概述
- 多项目并行管理和状态追踪
- 里程碑创建与进度监控
- 任务分配和优先级管理
- 项目时间线和截止日期提醒
- 任务依赖关系管理
- 项目进度报告生成

## 使用场景
- AI 助手帮助团队管理多个并行项目的进度
- 追踪软件开发各阶段里程碑完成情况
- 个人项目任务的智能化管理和提醒

## 依赖和前提条件
- Lofy AI 助手环境配置
- OpenClaw 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
