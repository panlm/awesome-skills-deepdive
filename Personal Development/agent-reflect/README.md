# reflect

> 通过对话分析进行自我改进，从纠正和成功模式中提取教训

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | reflect |
| **作者** | stevengonsalvez |
| **ClawHub** | https://clawskills.sh/skills/stevengonsalvez-agent-reflect |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stevengonsalvez/agent-reflect |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Signal Detection: Automatically identifies corrections with confidence levels (HIGH/MEDIUM/LOW)
- Category Classification: Routes learnings to appropriate agent files (Code Style, Architecture, Process, Domain, Tools)
- Skill Generation: Creates new skills from non-trivial debugging discoveries
- Metrics Tracking: Quantifies improvement with acceptance rates and statistics
- Human-in-the-Loop: All changes require explicit approval
- Git Integration: Full version control with easy rollback

## 依赖和前提条件
- Claude Code: `~/.claude/skills/reflect/`
- Clawdbot: `~/.clawdbot/skills/reflect/`

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `agent_mappings.md`
- `logs/` — 目录
- `signal_patterns.md`
- `skill.json` — 配置/数据文件

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23