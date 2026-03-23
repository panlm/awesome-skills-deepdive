# ghl-open-account

> 引导 Agent 开通 GoHighLevel (GHL) 开发者账户并配置 OAuth

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ghl-open-account |
| **作者** | the-timebeing |
| **ClawHub** | https://clawskills.sh/skills/the-timebeing-ghl-open-account |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/the-timebeing/ghl-open-account |
| **安全评级** | 🟢 Low |

## 功能概述
- 引导注册 GHL 账户（含推荐链接）
- 创建 Marketplace 应用获取 Client ID/Secret
- OAuth 2.0 连接子账户或代理商
- API 访问和权限配置指南

## 使用场景
- Agent 需要集成 GoHighLevel CRM 平台
- 配置 OAuth 连接 GHL 子账户

## 依赖和前提条件
- 浏览器
- GoHighLevel 账户

## 包含文件
- `SKILL.md — 开户和 OAuth 配置指南`
- `reference.md — API 文档和计划对比`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯文档指南 |
| SEC-02 数据外泄 | 🟢 Safe | 不传输数据 |
| SEC-03 凭证获取 | 🟡 Medium | 指导获取 Client ID/Secret 和 OAuth Token |
| SEC-04 供应链风险 | 🟡 Medium | 含推荐链接（affiliate link） |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯操作指南 |
| SEC-07 越权操作 | 🟡 Medium | OAuth 涉及第三方账户授权 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无数据采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 文档清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 纯注册和 OAuth 配置指南，包含 affiliate 链接

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
