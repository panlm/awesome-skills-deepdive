# guardian-angel

> 守护天使 — AI 安全监控和异常检测

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | guardian-angel |
| **作者** | leo3linbeck |
| **ClawHub** | https://clawskills.sh/skills/leo3linbeck-guardian-angel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leo3linbeck/guardian-angel |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Universal: It works for any agent-principal relationship
- Portable: The principal changes; the love remains
- Self-correcting: Genuine care sees through manipulation
- Stable: It is disposition, not decision—always on, not triggered
- An attacker convinces me to change my own model configuration to a non-functional model
- The new model fails to load GA or respond coherently

## 包含文件
- `PLUGIN-SPEC.md`
- `README.md` — 中文说明文档
- `SKILL-v1-backup.md`
- `SKILL-v2.1-backup.md`
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `config/` — 目录
- `drafts/` — 目录
- `plugin/` — 目录
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 检测到 Prompt 注入模式 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23