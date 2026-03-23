# bitwarden

> 设置和使用 Bitwarden CLI 进行密码库安全管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | bitwarden |
| **作者** | startupbros |
| **ClawHub** | https://clawskills.sh/skills/startupbros-bitwarden-vault |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/startupbros/bitwarden-vault |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- CRITICAL: Always run `bw` commands inside a dedicated tmux session. The CLI requires a session key (`BW_SESSION`) for all vault operations after authentication. A tmux session preserves this environment variable across commands.
- NEVER expose secrets in logs, code, or command output visible to users
- NEVER write secrets to disk unless absolutely necessary
- ALWAYS use `bw lock` when finished with vault operations
- PREFER reading secrets directly into environment variables or piping to commands
- If you receive "Vault is locked" errors, re-authenticate with `bw unlock`

## 依赖和前提条件
- 
- CRITICAL:** Always run `bw` commands inside a dedicated tmux session. The CLI requires a session key (`BW_SESSION`) for all vault operations after authentication. A tmux session preserves this environment variable across commands.
- Create a dedicated tmux session**: `tmux new-session -d -s bw-session`
- Attach and authenticate**: Run `bw login` or `bw unlock` inside the session
- [CLI Examples](references/cli-examples.md) - Common usage patterns and advanced operations

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

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