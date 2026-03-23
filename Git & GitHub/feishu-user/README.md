# feishu-user

> Feishu document operations (User Access Token version). Use user access token for authentication. When you need to read, create, write, or append Feishu documents.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feishu-user |
| **作者** | hacksing |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/hacksing-feishu-user |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hacksing/feishu-user |
| **安全评级** | 🟡 Medium |

## 功能概述
- APP_ID - App ID (from Feishu Open Platform app settings)
- APP_SECRET - App Secret (from Feishu Open Platform app settings)
- REDIRECT_URI - Authorization callback URL
- `docx:document` - Document operations
- `drive:drive.search:readonly` - Cloud drive search
- `search:docs:read` - Document search

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23