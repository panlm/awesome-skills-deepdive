# aaaaa

> This skill enables the agent to **automatically answer Gmail messages on behalf of a client**. The agent drafts and (when the user approves or when configured) sends replies using the client’s tone, s

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | aaaaa |
| **作者** | azvast |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/azvast-aa |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/azvast/aa |
| **安全评级** | 🟡 Medium |

## 功能概述
- The user asks to “reply to my emails,” “answer my Gmail,” or “draft responses to incoming mail.”
- The user provides a Gmail context (e.g. “inbox for client@example.com”) and wants automated or semi-automated replies.
- The user wants the agent to act as the client when responding to specific threads or senders.
- Gmail access: OAuth2 or app password for the client’s Gmail (never store raw passwords in the skill; use environment var
- Client profile (optional but recommended): short brief (tone, sign-off, topics they handle, topics to defer).
- Ask for or read the client’s brief: tone (formal/casual), sign-off (e.g. “Best,” “Thanks,”), and any “do not answer” or 

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `manifest.json`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23