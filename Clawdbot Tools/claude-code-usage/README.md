# claude-code-usage

> 检查 Claude Code OAuth API 用量限制（会话和周配额），支持自动监控和重置通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | claude-code-usage |
| **作者** | azaidi94 |
| **ClawHub** | https://clawskills.sh/skills/azaidi94-claude-code-usage |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/azaidi94/claude-code-usage |
| **安全评级** | 🟡 Medium |

## 功能概述
- 会话（5小时）和周（7天）用量追踪
- 美观的进度条和颜色状态指示
- 智能缓存（60秒默认）
- JSON 格式输出
- 自动监控和重置检测
- 会话刷新定时提醒

## 使用场景
- 检查 Claude Code 剩余用量
- 设置自动用量监控和提醒
- 将用量数据集成到状态栏

## 依赖和前提条件
curl, macOS Keychain 或 Linux secret-tool

## 包含文件
- `CRON_SETUP.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts/claude-usage.sh`
- `scripts/monitor-and-notify.sh`
- `scripts/monitor-usage.sh`
- `scripts/session-reminder.sh`
- `scripts/setup-monitoring.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 多个 Bash 脚本执行 curl 和系统命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向 api.anthropic.com 发送 OAuth 请求 |
| SEC-03 凭证获取 | 🔴 High | 从系统密钥链读取 Claude OAuth 令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖系统工具 curl/jq |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 /tmp 缓存文件和状态文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅查询 API 用量 |
| SEC-08 持久化机制 | 🟡 Medium | 支持 cron 和 launchd 定时任务 |
| SEC-09 信息采集 | 🟡 Medium | 获取 API 用量数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本逻辑清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 访问系统密钥链获取 OAuth 令牌，虽仅用于查询但涉及敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
