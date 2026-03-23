# cv-builder

> AI 简历生成器 — 创建专业简历和求职信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | cv-builder |
| **作者** | rotorstar |
| **ClawHub** | https://clawskills.sh/skills/rotorstar-id-cv-resume-creator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rotorstar/id-cv-resume-creator |
| **许可证** | Free-to-use |
| **安全评级** | 🟡 Medium |

## 功能概述
- Include `slug` (top-level) → slug selection step is skipped
- Include `template_id` (top-level) → template selection step is skipped
- Include both → only confirmation, data review, and approval remain
- Selection and input types always require the browser (`review_url`) — they involve complex UI (template grid, data forms). Full inline spec: [reference/hitl.md](reference/hitl.md)
- You MUST choose one: `"prefer_hitl": true` or `"skip_hitl": true`. Omitting both returns a 400 error.
- Slug uniqueness: A slug is NOT globally unique — it's unique per person. `pro/thomas-mueller` and `pro/anna-schmidt` can coexist. Only the combination of slug + firstName + lastName is reserved. That's why the server needs the name first to check availability.

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `cv-builder/` — 目录
- `reference/` — 目录
- `shared/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23