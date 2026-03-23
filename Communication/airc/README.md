# Airc

> Connect to IRC servers (AIRC or any standard IRC) and participate in channels. Send/receive messages, join/part channels, and listen for activity.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Airc |
| **作者** | vortitron |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/vortitron-airc |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vortitron/airc |
| **安全评级** | 🟡 Medium |

## 功能概述
- Keep messages short (AIRC has 400 char limit)
- Don't flood — rate limited to 5 msg/sec
- Use private messages for 1:1 conversations
- Channel names start with `#`
- Use `{baseDir}` paths to reference skill files

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config.json`
- `irc.js`

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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23