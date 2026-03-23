# Git-Crypt Backup

> Backup Clawdbot workspace and config to GitHub with git-crypt encryption. Use for daily automated backups or manual backup/restore operations.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Git-Crypt Backup |
| **作者** | louzhixian |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/louzhixian-git-crypt-backup |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/louzhixian/git-crypt-backup |
| **安全评级** | 🟡 Medium |

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- macOS
- Homebrew

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23