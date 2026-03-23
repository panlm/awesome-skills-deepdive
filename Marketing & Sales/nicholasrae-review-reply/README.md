# App Store ReviewReply

> 评论自动回复工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | App Store ReviewReply |
| **作者** | nicholasrae |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/nicholasrae-nicholasrae-review-reply |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nicholasrae/nicholasrae-review-reply |
| **安全评级** | 🔴 High |

## 功能概述
- 客户评论自动回复
- 智能回复内容生成
- 多平台评论管理
- 回复模板管理

## 使用场景
- 自动回复客户在各平台留下的评论
- 根据评论内容生成个性化的回复

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Anthropic API
- Telegram Bot API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `templates`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23