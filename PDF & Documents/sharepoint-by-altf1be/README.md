# SharePoint by altf1be

> "Secure SharePoint file operations and Office document intelligence via Microsoft Graph API — certificate auth, Sites.Selected, read/write Word (mammoth), Excel (exceljs), PowerPoint (jszip), PDF (pdf-parse)."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | SharePoint by altf1be |
| **作者** | abdelkrim |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/abdelkrim-sharepoint-by-altf1be |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/abdelkrim/sharepoint-by-altf1be |
| **安全评级** | 🔴 High |

## 功能概述
- [Features](#features)
- [Quick Start](#quick-start)
- [Setup](#setup)
- [Commands](#commands)
- [Supported File Formats](#supported-file-formats)
- [Security](#security)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- OAuth

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23