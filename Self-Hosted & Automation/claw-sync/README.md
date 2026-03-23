# claw-sync

> OpenClaw 记忆和工作区的安全同步工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | claw-sync |
| **作者** | arakichanxd |
| **ClawHub** | https://clawskills.sh/skills/arakichanxd-claw-sync |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/arakichanxd/claw-sync |
| **安全评级** | 🟡 Medium |

## 功能概述
- 版本化同步 OpenClaw 记忆文件和自定义 skills 到 Git 仓库
- 灾难恢复：每次恢复前自动创建本地备份
- 安全特性：不同步配置文件（API key 等），URL 验证，路径保护
- 支持 /sync、/restore、/sync-status、/sync-list 命令
- 跨平台支持（Windows/Mac/Linux）

## 使用场景
- 将 agent 记忆和配置安全备份到 GitHub
- 在新机器上快速恢复 agent 状态
- 版本化管理工作区变更

## 依赖和前提条件
- Node.js、Git
- GitHub/GitLab/Bitbucket 仓库和访问令牌
- 配置文件 `~/.openclaw/.backup.env`

## 包含文件
- `SKILL.md` — 技能定义和命令说明
- `index.js` — 主入口，命令路由
- `scripts/push.js` — 推送同步脚本
- `scripts/pull.js` — 拉取恢复脚本
- `scripts/setup-cron.js` — 定时同步设置
- `scripts/status.js` — 状态检查
- `config.example.env` — 配置示例
- `package.json` — Node.js 依赖

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 使用 child_process.spawn/execSync 执行 git 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 将工作区文件（MEMORY.md、SOUL.md 等）推送到远程 Git 仓库 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 .backup.env 中的 BACKUP_TOKEN（Git 访问令牌） |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Node.js 标准库，无 npm 依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | restore 操作会覆盖本地工作区文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 相关操作 |
| SEC-07 越权操作 | 🟢 Safe | 有 URL 验证（仅允许 GitHub/GitLab/Bitbucket）和路径保护 |
| SEC-08 持久化机制 | 🟡 Medium | 可设置 cron 定时同步 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理用户指定的工作区文件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，有安全特性说明 |

**综合评级: 🟡 Medium**
**风险摘要:** 将敏感工作区文件同步到远程仓库，但有安全过滤（不同步密钥/配置），整体风险可控

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
