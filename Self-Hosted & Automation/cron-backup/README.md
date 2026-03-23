# cron-backup

> 定时自动备份，支持版本跟踪和自动清理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | cron-backup |
| **作者** | zfanmy |
| **ClawHub** | https://clawskills.sh/skills/zfanmy-cron-backup |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zfanmy/cron-backup |
| **安全评级** | 🟢 Low |

## 功能概述
- 创建带时间戳的 tar.gz 备份归档
- 版本触发备份：仅在版本变更时备份
- 系统 cron 集成，支持自定义调度
- 自动清理过期备份，防止磁盘空间耗尽
- 保留文件权限和目录结构
- 排除常见临时文件（node_modules、.git 等）

## 使用场景
- 定期自动备份目录或项目
- 在软件版本更新时自动触发备份
- 管理备份保留策略（如保留最近7天）

## 依赖和前提条件
- bash、tar、cron

## 包含文件
- `SKILL.md` — 技能定义
- `scripts/backup.sh` — 单次备份执行
- `scripts/backup-versioned.sh` — 版本触发备份
- `scripts/setup-cron.sh` — cron 任务设置
- `scripts/cleanup.sh` — 旧备份清理
- `scripts/list-backups.sh` — 列出可用备份

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 tar、mkdir、date 等标准命令，参数来自用户传入 |
| SEC-02 数据外泄 | 🟢 Safe | 仅本地备份，不发送到外部 |
| SEC-03 凭证获取 | 🟢 Safe | 不处理凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 bash 脚本，无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅创建备份文件和删除过期备份 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 在用户指定目录内操作 |
| SEC-08 持久化机制 | 🟡 Medium | 修改系统 crontab 添加定时任务 |
| SEC-09 信息采集 | 🟢 Safe | 不采集系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 简洁的本地备份工具，仅修改 crontab，无网络操作，风险极低

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
