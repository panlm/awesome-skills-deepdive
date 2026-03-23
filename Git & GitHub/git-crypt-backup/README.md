# Git-Crypt Backup

> 使用 git-crypt 加密将 Clawdbot 工作区和配置自动备份到 GitHub，支持每日自动备份和手动备份/恢复操作。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git-Crypt Backup |
| **作者** | louzhixian |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/louzhixian-git-crypt-backup |

## 功能概述
- 将 `~/clawd`（工作区）和 `~/.clawdbot`（配置）自动备份到 GitHub 私有仓库
- 使用 git-crypt 对敏感文件（SOUL.md、USER.md、MEMORY.md、凭证等）进行加密
- 提供自动化备份脚本 `scripts/backup.sh`，支持 cron 定时任务
- 支持在新机器上通过密钥解锁快速恢复
- 通过 `.gitattributes` 精细控制哪些文件加密、哪些明文
- 通过 `.gitignore` 排除不需要备份的文件（日志、媒体、浏览器缓存等）

## 使用场景
- 定期自动备份 Clawdbot 的工作区和配置到 GitHub，防止数据丢失
- 在新设备上快速恢复 Clawdbot 环境（克隆 + 解锁密钥即可）
- 安全地将包含敏感信息的配置文件存储到远程仓库

## 依赖和前提条件
- `git-crypt`：加密工具（macOS: `brew install git-crypt`，Linux: `apt install git-crypt`）
- `git`：版本控制
- GitHub 账户和 SSH 密钥配置
- 需要安全保存 git-crypt 导出的密钥文件（推荐 1Password、iCloud Keychain 等）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
