# opsecmd

> 操作安全(OPSEC)提醒指南，面向 AI Agent 和人类用户的安全意识教育

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | opsecmd |
| **作者** | wulf715 |
| **ClawHub** | https://clawskills.sh/skills/wulf715-opsecmd |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/wulf715/opsecmd |
| **安全评级** | 🟢 Low |

## 功能概述
- Agent 安全行为准则
- 人类用户安全审查指南
- Skill 代码审查建议
- 运行未知代码的风险警示
- heartbeat 定期提醒机制

## 使用场景
- 提升 Agent 运行安全意识
- 提醒用户审查 Skill 代码
- 定期安全检查

## 依赖和前提条件
- 无（纯文本 Skill）

## 包含文件
skill.md（主指南）, heartbeat.md（定期提醒）, versioning.txt（版本日志）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无代码执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 纯教育内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯安全教育文档，讽刺的是本身完全无害

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
