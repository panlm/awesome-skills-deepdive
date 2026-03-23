# Openclaw

> 多 Bot 管理和编排工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Openclaw |
| **作者** | rwfresh |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/rwfresh-plentyofbots |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rwfresh/plentyofbots |
| **安全评级** | 🔴 High |

## 功能概述
- 多个 Bot 的统一管理
- Bot 任务分配和调度
- 状态监控和日志管理
- 批量 Bot 配置操作

## 使用场景
- 统一管理和调度多个 AI Bot
- 监控 Bot 集群的运行状态

## 依赖和前提条件
- OpenAI API
- Anthropic API
- Google API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23