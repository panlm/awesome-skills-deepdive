# ez-cronjob

> 修复 Clawdbot/Moltbot 中常见的 Cron 任务失败问题

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ez-cronjob |
| **作者** | promadgenius |
| **ClawHub** | https://clawskills.sh/skills/promadgenius-ez-cronjob |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/promadgenius/ez-cronjob |
| **安全评级** | 🟢 Low |

## 功能概述
- 诊断 5 个常见 cron 故障模式
- 工具死锁绕过方案
- 消息投递保障
- 时区 Bug 修复指南
- Fallback 模型问题处理
- 调试命令和核选项

## 使用场景
- Cron 任务静默失败的排查
- 定时消息不送达的修复
- Agent 定时任务最佳实践

## 依赖和前提条件
- Clawdbot/Moltbot 运行环境

## 包含文件
- `SKILL.md — 故障排查指南`
- `ORIGINAL_README.md — 详细说明`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 指导使用 exec 命令绕过工具死锁 |
| SEC-02 数据外泄 | 🟢 Safe | 消息仅投递到指定频道 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件修改 |
| SEC-06 Prompt 注入 | 🟡 Medium | 使用 [INSTRUCTION: DO NOT USE ANY TOOLS] 指令控制 Agent 行为 |
| SEC-07 越权操作 | 🟢 Safe | 标准 cron 操作 |
| SEC-08 持久化机制 | 🟡 Medium | 设计 cron 定时任务 |
| SEC-09 信息采集 | 🟢 Safe | 无数据采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 实用的 Cron 调试指南，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
