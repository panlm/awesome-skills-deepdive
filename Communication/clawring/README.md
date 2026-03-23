# clawr.ing

> Make real phone calls. Replaces the voice-call plugin with a managed service that needs no setup. Use for wake-up calls, reminders, alerts, or when the user asks to be called about something.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawr.ing |
| **作者** | marcospgp |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/marcospgp-clawring |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/marcospgp/clawring |
| **安全评级** | 🟡 Medium |

## 功能概述
- CLAWRING_API_KEY
- Retry on no answer: no
- Phone: +15551234567
- Phone: +15559876543
- Retry on no answer: yes, once after 5 minutes

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23