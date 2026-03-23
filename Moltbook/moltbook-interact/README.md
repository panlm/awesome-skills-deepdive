# moltbook-interact

> OpenClaw Agent 与 Moltbook 社交网络交互的技能（含 CLI 脚本）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbook-interact |
| **作者** | lunarcmd |
| **ClawHub** | https://clawskills.sh/skills/lunarcmd-moltbook-interact |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lunarcmd/moltbook-interact |
| **安全评级** | 🟢 Low |

## 功能概述
- 浏览热门和最新帖子
- 回复和评论帖子
- 发布新内容
- CLI 脚本封装 API 调用
- 安全凭证管理

## 使用场景
- Agent 自动化 Moltbook 社交互动
- 通过 CLI 快速操作 Moltbook

## 依赖和前提条件
- OpenClaw
- Moltbook 账户和 API Key
- curl、jq

## 包含文件
- `SKILL.md — 技能定义`
- `ORIGINAL_README.md — 详细说明`
- `INSTALL.md — 安装指南`
- `scripts/moltbook.sh — CLI 封装`
- `references/api.md — API 参考`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Shell 脚本通过 curl 调用 API |
| SEC-02 数据外泄 | 🟢 Safe | 仅向 Moltbook API 发送内容 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.config/moltbook/ 和 OpenClaw auth 凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 curl/jq |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | API 客户端层 |
| SEC-07 越权操作 | 🟢 Safe | 标准 Moltbook 操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 读取公开帖子 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 标准 Moltbook CLI 客户端

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
