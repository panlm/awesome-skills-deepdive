# Google Docs Skill

> Direct access to the Google Docs API using OAuth 2.0. Create documents, insert and format text, and manage document content.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Google Docs Skill |
| **作者** | zagran |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/zagran-google-docs-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zagran/google-docs-skill |
| **安全评级** | 🔴 High |

## 功能概述
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Create a new project or select existing one
- Enable the Google Docs API
- Create OAuth 2.0 credentials (Desktop app or Web application)
- Download the credentials JSON file
- Indices are 1-based (document starts at index 1)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23