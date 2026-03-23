# QRdex

> Create, manage, and track QR codes using the QRdex.io REST API. Use when working with QR code generation, URL shortening with QR codes, WiFi QR codes, email/SMS/WhatsApp QR codes, scan tracking, or any QRdex.io operations. Supports all QR types (url, email, telephone, sms, whatsapp, wifi) with customizable colors and shapes.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | QRdex |
| **作者** | sebastienb |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/sebastienb-qrdex |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sebastienb/qrdex |
| **安全评级** | 🟡 Medium |

## 功能概述
- `foreground_color` — hex color (default: `#000000`)
- `background_color` — hex color (default: `#FFFFFF`)
- `shape` — QR code shape (default: `rounded`)
- `track_scans` — enable scan tracking (default: `true`)
- `401` — Invalid/missing API key
- `403` — No permission

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23