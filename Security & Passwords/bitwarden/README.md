# bitwarden

> 通过 rbw CLI 安全访问和管理 Bitwarden/Vaultwarden 密码

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | bitwarden |
| **作者** | asleep123 |
| **ClawHub** | https://clawskills.sh/skills/asleep123-bitwarden |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/asleep123/bitwarden |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Note: Login requires the Master Password and potentially 2FA (email/TOTP).*
- Note: `rbw` caches the session key in the agent. If interactive input is required (pinentry), see if you can setup `pinentry-curses` (CLI-based pinentry) as the pinentry provider.*
- List items: `rbw list`
- Get item: `rbw get "Name"`
- Get JSON: `rbw get --full "Name"`
- Search: `rbw search "query"`

## 依赖和前提条件
- Note: Login requires the Master Password and potentially 2FA (email/TOTP).*

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
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