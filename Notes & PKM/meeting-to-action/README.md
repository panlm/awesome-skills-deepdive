# Meeting To Action

> Convert meeting notes or transcripts into clear summaries, decisions, and action items with owners and due dates. Use when a user asks to turn a meeting recording, transcript, or notes into a follow-up plan.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Meeting To Action |
| **作者** | codedao12 |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawskills.sh/skills/codedao12-meeting-to-action |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/codedao12/meeting-to-action |
| **安全评级** | 🟢 Low |

## 功能概述
- Use when the user provides a transcript or detailed notes.
- Use when the user needs action items, decisions, and next steps.
- Use when a concise recap email or message is required.
- Avoid when the user wants tasks or calendar invites created automatically.
- Avoid when the transcript is missing and cannot be summarized reliably.
- Avoid when sensitive content should not be shared.

## 使用场景
- 管理个人笔记和知识
- 自动化信息整理
- 构建个人知识管理系统

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23