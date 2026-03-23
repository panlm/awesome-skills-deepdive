# Mediator

> Intercept and filter communications from difficult contacts. Strips emotion, extracts facts, drafts neutral responses. Use when setting up communication filtering for specific contacts, configuring the mediator, or processing intercepted messages. Triggers on "mediator", "intercept messages", "filter communications", "difficult contact", or requests to handle messages from someone the user doesn't want to deal with directly.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mediator |
| **作者** | dylntrnr |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/dylntrnr-mediator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dylntrnr/mediator |
| **安全评级** | 🟢 Low |

## 功能概述
- name: "Ex Partner"
- name: "Difficult Client"
- intercept: Archive/hide original, only show summary. User never sees raw emotional content.
- assist: Show original but also provide summary and response suggestions.
- facts-only: Extract only actionable items, requests, deadlines. No emotion.
- neutral: Rewrite the message in neutral tone, preserving all content.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23