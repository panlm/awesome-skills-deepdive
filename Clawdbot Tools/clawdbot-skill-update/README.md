# clawdbot-skill-update

> Clawdbot 全面备份、更新和恢复工作流，支持动态工作空间检测

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdbot-skill-update |
| **作者** | pasogott |
| **ClawHub** | https://clawskills.sh/skills/pasogott-clawdbot-skill-update |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pasogott/clawdbot-skill-update |
| **安全评级** | 🟡 Medium |

## 功能概述
- 配置/会话/凭证完整备份
- 动态检测所有代理工作空间
- 多代理支持
- 安全回滚恢复
- Git 版本追踪
- 预览模式（dry-run）

## 使用场景
- Clawdbot 大版本更新前备份
- 更新失败后回滚恢复
- 多代理环境的批量备份

## 依赖和前提条件
bash, jq, tar, git

## 包含文件
- `PUBLISH.md`
- `QUICK_REFERENCE.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `TEST.md`
- `UPDATE_CHECKLIST.md`
- `_meta.json`
- `backup-clawdbot-dryrun.sh`
- `backup-clawdbot-full.sh`
- `check-upstream.sh`
- `config.json`
- `package.json`
- `restore-clawdbot.sh`
- `validate-setup.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 多个 Bash 脚本执行 tar/cp/git 等命令 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络通信 |
| SEC-03 凭证获取 | 🟡 Medium | 备份包含凭证和认证令牌文件 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖系统工具 |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建备份目录，恢复时覆盖配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 恢复操作会覆盖现有配置 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 备份所有配置和凭证数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本逻辑清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 备份恢复工具涉及敏感凭证文件操作，恢复时覆盖现有配置

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
