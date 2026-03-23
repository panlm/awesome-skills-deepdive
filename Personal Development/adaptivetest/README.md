# adaptive-testing

> 基于项目反应理论(IRT)的自适应测试系统设计

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | adaptive-testing |
| **作者** | woodstocksoftware |
| **ClawHub** | https://clawskills.sh/skills/woodstocksoftware-adaptivetest |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/woodstocksoftware/adaptivetest |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Key advantage: Traditional tests waste time on too-easy or too-hard questions. Adaptive tests spend time where measurement matters most — near the student's ability level.
- a (discrimination) — How well the question differentiates ability levels. Higher = steeper curve. Typical range: 0.5 to 2.5
- b (difficulty) — The ability level where P(correct) = 0.5. Range: -3 to +3 (standardized scale)
- c (guessing) — Probability of guessing correctly. Usually 0.2 to 0.25 for multiple choice
- Probability of correct response:
- Simpler models:

## 依赖和前提条件
- 
- Item bank: 300 questions, b from -2 (basic) to +2 (advanced)
- Target: SE < 0.35 or max 25 questions
- Content: 40% algebra, 30% geometry, 30% statistics
- Algorithm: Randomesque (top 5), EAP estimation

## 包含文件
- `BUILD-BRIEF.md`
- `CHANGELOG.md`
- `CLAUDE.md`
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `clawhub.json` — 配置/数据文件
- `references/` — 目录
- `specs/` — 目录

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