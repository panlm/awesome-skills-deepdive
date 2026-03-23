# Humanizer

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Humanizer |
| **作者** | brandonwise |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/brandonwise-ai-humanizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brandonwise/ai-humanizer |
| **安全评级** | 🟡 Medium |

## 功能概述
- Tier 1 (Dead giveaways): 50+ words that appear 5-20x more in AI text. Always flagged. Examples: *delve, tapestry, vibran
- Tier 2 (Suspicious in density): 80+ words flagged when 2+ appear. Examples: *furthermore, paradigm, holistic, utilize, f
- Tier 3 (Context-dependent): 60+ words flagged only at >3% density. Examples: *significant, effective, unique, compelling
- Phrases: 80+ multi-word patterns. Examples: *"In today's digital age"*, *"plays a crucial role"*, *"serves as a testamen
- Vary sentence length (short, then long, then short)
- Have opinions and take stances

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `assets`
- `docs`
- `eslint.config.js`
- `package.json`
- `references`
- `scripts`
- `src`
- `tests`
- `vitest.config.js`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23