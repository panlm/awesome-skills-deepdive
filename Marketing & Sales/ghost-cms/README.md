# Ghost CMS

> Ghost CMS 内容管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ghost CMS |
| **作者** | chrisagiddings |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/chrisagiddings-ghost-cms |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chrisagiddings/ghost-cms |
| **安全评级** | 🔴 High |

## 功能概述
- Ghost CMS 文章发布和管理
- 内容编辑和格式化
- 会员和订阅管理
- SEO 配置优化

## 使用场景
- 通过 AI 助手在 Ghost CMS 上管理博客内容
- 自动化 Ghost CMS 的内容发布流程

## 依赖和前提条件
- API 密钥
- Node.js
- npm
- GitHub API
- Notion API
- Webhook 配置

## 包含文件
- `LEXICAL-MIGRATION.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `references`
- `scripts`
- `snippets`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 6 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23