# email-management-expert

> macOS 邮件管理技能 — 搜索、分类和处理邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | email-management-expert |
| **作者** | latisen |
| **ClawHub** | https://clawskills.sh/skills/latisen-skill-email-management |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/latisen/skill-email-management |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Apple Mail MCP = The tools (18 email management functions)
- Email Management Skill = The expertise (workflows, strategies, best practices)
- Daily Inbox Triage - Process emails quickly (10-15 min)
- Inbox Zero - Achieve and maintain empty inbox
- Email Organization - Folder structures and filing strategies
- Advanced Search - Find any email quickly

## 依赖和前提条件
- Download `email-management-skill.zip` from the [releases page](https://github.com/patrickfreyer/apple-mail-mcp/releases)
- That's it! The skill is now available in Claude Code.
- User Scope (Recommended):**
- Trigger Keywords:**
- "inbox management"

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `examples/` — 目录
- `templates/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23