# Self Review

> Automatically review agent output quality before sending to user.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Self Review |
| **作者** | leic8959-sudo |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/leic8959-sudo-self-review |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leic8959-sudo/self-review |
| **安全评级** | 🟢 Low |

## 功能概述
- Length: 太短 (<100 chars) → warn
- HasAction: 包含行动词（应该/需要/建议/请）→ pass
- Clarity: 行数 >3 → pass (结构清晰)
- Combined score < 0.7 → reject
- [ ] 使用 LLM API 进行语义质量评估（而非规则）
- [ ] 添加 token 计数和压缩建议

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
- `index.js`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23