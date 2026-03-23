# Fastmail

> Manages Fastmail email and calendar via JMAP and CalDAV APIs. Use for emails (read, send, reply, search, organize, bulk operations, threads) or calendar (events, reminders, RSVP invitations). Timezone auto-detected from system.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Fastmail |
| **作者** | witooh |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawskills.sh/skills/witooh-fastmail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/witooh/fastmail |
| **安全评级** | 🔴 High |

## 功能概述
- Default: Auto-detects your system's local timezone
- Input: Accept times in configured timezone format
- Storage: Stored as UTC internally
- Display: Converted to configured timezone for display
- DST: Handles Daylight Saving Time automatically
- You say: "สร้างนัด 10:00" (assumed local timezone)

## 使用场景
- 设置和管理提醒事项
- 跟踪待办任务
- 通过自然语言创建提醒

## 依赖和前提条件
- API Key

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `dist`
- `package.json`
- `references`
- `scripts`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23