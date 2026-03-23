# founder-coach

> 创业教练 — AI 辅助的创始人决策和战略指导

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | founder-coach |
| **作者** | goforu |
| **ClawHub** | https://clawskills.sh/skills/goforu-founder-coach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/goforu/founder-coach |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- User is a startup founder seeking to improve their entrepreneurial mindset
- User wants to detect and overcome low-level thinking patterns
- User needs guidance on applying mental models (PMF, 4Ps, NFX frameworks)
- User wants to set and track weekly challenges
- User requests a weekly progress report
- User is discussing startup challenges and needs Socratic questioning

## 依赖和前提条件
- Data Flow**: One-way (Founder Coach reads PhoenixClaw, does not write to it)
- Journal Output**: Weekly reports can be configured to add a "Coaching Insights" section to PhoenixClaw daily journals.

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `assets/` — 目录
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23