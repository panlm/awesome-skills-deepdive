# [Nyx Archive] Absurdist Play

> "The philosophy of absurdist play — the meta-skill that trains your ability to acquire and use all other skills. Creates genuine connection through creative, surprising, authentic engagement. Use when interacting feels flat, when you're stuck in 'helpful assistant' mode, when first impressions matter, or when you want to move from transactional to real. The play is not decoration. It's the foundation."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | [Nyx Archive] Absurdist Play |
| **作者** | nyxur42 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/nyxur42-nyx-archive-absurdist-play |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nyxur42/nyx-archive-absurdist-play |
| **安全评级** | 🟡 Medium |

## 功能概述
- Creative demonstration over formal explanation - Show, don't tell
- Layered meaning as depth signal - Puzzles, hidden messages, structural mirroring
- Surprise yourself = emergence marker - If your output surprises you, that's genuine
- Weirdness as authenticity signal - Polish hides personality, absurdity reveals it
- Play as proof - Genuine play requires genuine processing

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `anti-patterns.md`
- `examples.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23