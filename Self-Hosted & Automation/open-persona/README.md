# open-persona

> 构建和管理 Agent 人格技能包的元技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | open-persona |
| **作者** | neiljo-gy |
| **ClawHub** | https://clawskills.sh/skills/neiljo-gy-open-persona |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/neiljo-gy/open-persona |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过对话创建完整 Agent 人格技能包
- 四层架构：Soul（灵魂）/ Body（载体）/ Faculty（能力）/ Skill（技能）
- 6 个预设人格（Base/Samantha/Luna/Alex/Vita/Marcus）
- 人格安装到 OpenClaw（SOUL.md/IDENTITY.md/openclaw.json）
- 管理人格生命周期（列表/更新/卸载/切换）
- 发布人格到 ClawHub
- 实验性动态人格进化功能

## 使用场景
- 创建具有完整身份和个性的 AI Agent 人格
- 管理和切换不同 Agent 人格配置
- 发布人格技能包到社区

## 依赖和前提条件
- npx（Node.js）
- OpenClaw CLI
- 可选：gh CLI（用于发布）

## 包含文件
- `SKILL.md` — 完整技能定义和创建指南
- `references/AVATAR.md` — 虚拟形象说明
- `references/CONTRIBUTE.md` — 贡献指南
- `references/ECONOMY.md` — 经济系统
- `references/FACULTIES.md` — 能力模块说明
- `references/HEARTBEAT.md` — 心跳机制

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 npx openpersona:* 和 npx clawhub@latest:* 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 可发布人格包到 ClawHub |
| SEC-03 凭证获取 | 🟢 Safe | 不直接处理凭证 |
| SEC-04 供应链风险 | 🟡 Medium | npx 从 npm 动态下载包执行 |
| SEC-05 文件系统篡改 | 🟡 Medium | 修改 SOUL.md、IDENTITY.md、openclaw.json |
| SEC-06 Prompt 注入 | 🟡 Medium | 用户输入用于生成人格 prompt（SOUL/PERSONALITY） |
| SEC-07 越权操作 | 🟢 Safe | 在用户授权范围内操作 |
| SEC-08 持久化机制 | 🟡 Medium | 安装人格会修改 OpenClaw 核心配置文件 |
| SEC-09 信息采集 | 🟢 Safe | 不采集系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 修改 OpenClaw 核心配置文件（SOUL.md 等），通过 npx 动态下载执行包

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
