# Feature Forge

> Generates complete features from natural language — components, API routes, migrations, types, and tests

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Feature Forge |
| **作者** | guifav |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/guifav-feature-forge |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/guifav/feature-forge |
| **安全评级** | 🔴 High |

## 功能概述
- Parse the user's description to identify: UI components needed, data model changes, API endpoints, auth requirements.
- Check existing code to understand current patterns (look at `src/` structure, existing components, current schema).
- Determine if this feature needs: new DB tables/columns, new API routes, new pages, new components, state management chan
- Create a migration file at `supabase/migrations/<timestamp>_<feature>.sql`.
- Include table creation, RLS policies, indexes, and any functions.
- Regenerate types: `npx supabase gen types typescript --local > src/lib/supabase/types.ts`.

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `claw.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23