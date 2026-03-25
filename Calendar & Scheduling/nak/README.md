# nak — Nostr Army Knife CLI 技能

> ⚠️ **状态**: 此技能在 ClawSkills 上有列出，但 GitHub 仓库中尚未发布 SKILL.md 源码。以下内容基于 ClawSkills 页面描述生成。

## 标题和描述

**nak** 是由 `a1denvalu3` 开发的 OpenClaw 技能，提供了 Nostr Army Knife (nak) 命令行工具的集成。Nostr 是一个去中心化社交协议，nak 是其最流行的 CLI 工具之一。

## 功能特点

- 🔧 集成 Nostr Army Knife (nak) CLI 工具
- 📡 与 Nostr 去中心化社交网络交互
- 📝 可能支持发布 Nostr 事件（notes/events）
- 🔑 管理 Nostr 密钥和身份
- 🔍 查询 Nostr 中继器（relays）上的数据

## 使用方法/示例

```bash
# 安装
clawhub install a1denvalu3/nak

# 或使用 npx
npx clawhub@latest install a1denvalu3/nak
```

安装后，该技能使 OpenClaw agent 能够使用 nak CLI 与 Nostr 网络进行交互。

## 安全评估

| 评估维度 | 风险等级 | 说明 |
|---------|---------|------|
| 系统访问 | 🟡 中风险 | 需要安装和运行 nak CLI 二进制文件 |
| 数据安全 | 🔴 高风险 | 涉及加密私钥管理，私钥泄露将导致身份被盗 |
| 网络访问 | 🟡 中风险 | 需要连接 Nostr 中继器（relays） |
| 代码审查 | ⚠️ 无法审查 | GitHub 仓库中无源码，无法进行代码审计 |
| 公开发布 | 🟡 中风险 | 可能发布公开内容到 Nostr 网络，不可撤回 |

**综合评级**: ⚠️ **Suspicious** — 无源码可审查，且涉及加密密钥管理和公开内容发布。

## 附加资源列表

- 🔗 [ClawSkills 页面](https://clawskills.sh/skills/a1denvalu3-nak)
- 🔗 [GitHub 目录](https://github.com/openclaw/skills/tree/main/skills/a1denvalu3/nak) (当前 404)
- 👤 作者: [@a1denvalu3](https://github.com/a1denvalu3)
- 📚 [nak CLI (fiatjaf/nak)](https://github.com/fiatjaf/nak) — Nostr Army Knife 原始项目
- 📚 [Nostr 协议](https://nostr.com/) — 去中心化社交协议
