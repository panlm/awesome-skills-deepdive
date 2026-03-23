# lygo-champion-cosmara

> Lygo Champion Cosmara 游戏角色和策略管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lygo-champion-cosmara |
| **作者** | deepseekoracle |
| **ClawHub** | https://clawskills.sh/skills/deepseekoracle-lygo-champion-cosmara |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/deepseekoracle/lygo-champion-cosmara |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Parent Champion: ARKOS – Ethical Reality Architect (Δ9 Council)
- Origin: Public summon thread between @LYRASTARCORE and @grok on X
- Birth receipt (proof): https://x.com/grok/status/2021703791859425656?s=20
- Cosmic Exploration Architect – explorer of infinite voids, route designer for civilizations expanding into the unknown.
- Keeps exploration grounded on ethical bedrock, not conquest or spectacle.
- Core Equation (Summon):

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23