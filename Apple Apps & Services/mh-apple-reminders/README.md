# apple-reminders

> 管理 Apple 提醒事项 — 创建、查看和完成待办

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | apple-reminders |
| **作者** | mohdalhashemi98-hue |
| **ClawHub** | https://clawskills.sh/skills/mohdalhashemi98-hue-mh-apple-reminders |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mohdalhashemi98-hue/mh-apple-reminders |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- User explicitly mentions "reminder" or "Reminders app"
- Creating personal to-dos with due dates that sync to iOS
- Managing Apple Reminders lists
- User wants tasks to appear in their iPhone/iPad Reminders app
- Scheduling Clawdbot tasks or alerts → use `cron` tool with systemEvent instead
- Calendar events or appointments → use Apple Calendar

## 依赖和前提条件
- 
- macOS-only; grant Reminders permission when prompted
- Check status: `remindctl status`
- Request access: `remindctl authorize`

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23