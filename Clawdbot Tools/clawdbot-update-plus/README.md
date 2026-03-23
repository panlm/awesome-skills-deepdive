# clawdbot-update-plus

> Clawdbot 全环境备份、更新和恢复工具，支持加密和云同步

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdbot-update-plus |
| **作者** | hopyky |
| **ClawHub** | https://clawskills.sh/skills/hopyky-clawdbot-update-plus |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hopyky/clawdbot-update-plus |
| **安全评级** | 🟡 Medium |

## 功能概述
- 完整环境备份（配置/工作空间/技能）
- 自动回滚失败更新
- GPG 加密备份
- rclone 云存储同步
- 多目录技能更新
- WhatsApp/Telegram/Discord 通知

## 使用场景
- 自动化 Clawdbot 日常更新
- 加密备份到云存储
- 更新失败时自动回滚

## 依赖和前提条件
git, jq, rsync (必需); rclone, gpg (可选)

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `bin/lib/backup.sh`
- `bin/lib/config.sh`
- `bin/lib/cron.sh`
- `bin/lib/notify.sh`
- `bin/lib/restore.sh`
- `bin/lib/update.sh`
- `bin/lib/utils.sh`
- `clawdbot-update.example.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 7 个模块化 Bash 脚本，执行 git/tar/rsync 等 |
| SEC-02 数据外泄 | 🟡 Medium | rclone 云同步，通知发送 |
| SEC-03 凭证获取 | 🟡 Medium | 备份包含凭证，GPG 密钥配置 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖系统工具 |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建/恢复备份，修改 crontab |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 恢复操作覆盖配置，cron 安装 |
| SEC-08 持久化机制 | 🟡 Medium | 支持 cron 定时自动更新 |
| SEC-09 信息采集 | 🟡 Medium | 备份所有环境数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 模块化代码清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 功能完善的备份更新工具，涉及凭证操作和持久化定时任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
