# moltbot-security

> Moltbot/Clawdbot 安全加固指南

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbot-security |
| **作者** | nextfrontierbuilds |
| **ClawHub** | https://clawskills.sh/skills/nextfrontierbuilds-moltbot-security |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-security |
| **安全评级** | 🟢 Low |

## 功能概述
- 绑定 loopback 避免公开暴露
- 设置认证 Token
- 修复文件权限
- Node.js 版本要求
- Tailscale 安全远程访问
- 基于 Shodan 研究的真实漏洞数据

## 使用场景
- 新部署的 Moltbot 安全加固
- 检查现有部署的安全状态
- 修复已知安全问题

## 依赖和前提条件
- Clawdbot/Moltbot 环境

## 包含文件
- `SKILL.md — 安全配置指南`
- `ORIGINAL_README.md — 详细说明和安全模板`
- `package.json — npm 元数据`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 指导运行 security audit 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 安全加固不传输数据 |
| SEC-03 凭证获取 | 🟢 Safe | 指导保护凭证而非获取 |
| SEC-04 供应链风险 | 🟢 Safe | 无代码依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 修改配置文件和文件权限 |
| SEC-06 Prompt 注入 | 🟢 Safe | 安全指南 |
| SEC-07 越权操作 | 🟢 Safe | 目的是减少越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 审计是安全行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰透明 |

**综合评级: 🟢 Low**
**风险摘要:** 优秀的安全加固指南，对生态有积极贡献

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
