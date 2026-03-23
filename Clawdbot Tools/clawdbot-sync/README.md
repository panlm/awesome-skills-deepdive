# clawdbot-sync

> 通过 SSH/rsync 在多个 Clawdbot 实例间同步记忆、偏好和技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawdbot-sync |
| **作者** | udiedrichsen |
| **ClawHub** | https://clawskills.sh/skills/udiedrichsen-clawdbot-sync |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/clawdbot-sync |
| **安全评级** | 🟡 Medium |

## 功能概述
- 双向同步内存和配置文件
- 智能冲突解决（时间戳优先）
- 选择性同步
- Tailscale 节点发现
- Dry-run 预览模式
- 同步历史记录

## 使用场景
- 多台设备间同步 Clawdbot 记忆
- Mac 和服务器之间共享偏好设置
- 团队协作的代理配置同步

## 依赖和前提条件
rsync, ssh, jq, Tailscale（可选）

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references/setup.md`
- `scripts/handler.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Bash 脚本执行 rsync 和 ssh 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 通过 SSH/rsync 与远程主机通信 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 SSH 密钥认证 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖系统工具 |
| SEC-05 文件系统篡改 | 🟡 Medium | 同步写入记忆和配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可推送/拉取远程机器的文件 |
| SEC-08 持久化机制 | 🟡 Medium | 支持自动同步模式 |
| SEC-09 信息采集 | 🟡 Medium | 同步所有记忆文件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本清晰可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及远程文件同步，需信任目标主机和网络环境

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
