# claude-connect

> 将 Claude 订阅连接到 Clawdbot 并自动刷新 OAuth 令牌（已弃用）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | claude-connect |
| **作者** | tunaissacoding |
| **ClawHub** | https://clawskills.sh/skills/tunaissacoding-claude-connect |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tunaissacoding/claude-connect |
| **安全评级** | 🔴 High |

## 功能概述
- 从 macOS Keychain 读取 Claude OAuth 令牌
- 写入 Clawdbot auth-profiles.json
- 每 2 小时自动刷新令牌
- 成功/失败通知
- 自动检测通知目标
- 一键安装/卸载

## 使用场景
- （已弃用）连接 Claude CLI 到 Clawdbot
- Clawdbot 已内置此功能，无需此 skill

## 依赖和前提条件
macOS, Claude CLI, jq, launchd

## 包含文件
- `AUTO-DETECTION-FLOW.md`
- `CHANGELOG.md`
- `CHANGES.md`
- `COMPLETION-REPORT.md`
- `DELIVERABLES.txt`
- `DETECTION-EXAMPLES.md`
- `QUICKSTART.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `SUMMARY.md`
- `UPGRADE.md`
- `_meta.json`
- `claude-oauth-refresh-config.example.json`
- `detect-notification-config.sh`
- `install.sh`
- `refresh-token.sh`
- `test-detection.sh`
- `uninstall.sh`
- `validate-update.sh`
- `verify-setup.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 多个 Shell 脚本执行系统命令，包括 launchctl 和 security 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Anthropic token URL 发送刷新请求 |
| SEC-03 凭证获取 | 🔴 High | 直接读取 Keychain 凭证并写入 auth-profiles.json |
| SEC-04 供应链风险 | 🟢 Safe | 依赖系统工具 |
| SEC-05 文件系统篡改 | 🔴 High | 写入 ~/.clawdbot/agents/main/agent/auth-profiles.json |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 修改 Clawdbot 认证配置 |
| SEC-08 持久化机制 | 🔴 High | 安装 launchd 持久化任务，每 2 小时运行 |
| SEC-09 信息采集 | 🟡 Medium | 读取 Keychain 和会话数据检测通知目标 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本清晰可审计 |

**综合评级: 🔴 High**
**风险摘要:** 直接操作系统密钥链和认证文件，安装持久化定时任务；且已被官方弃用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
