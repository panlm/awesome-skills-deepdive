# Feishu Card

> 飞书卡片消息构建和发送工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Feishu Card |
| **作者** | autogame-17 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/autogame-17-feishu-card |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-card |
| **安全评级** | 🟢 Low |

## 功能概述
- 构建飞书互动卡片消息
- 支持多种卡片元素和布局
- 卡片模板管理
- 通过 Webhook 发送卡片

## 使用场景
- 构建项目进度通知的互动卡片消息
- 创建包含操作按钮的飞书审批卡片

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `TROUBLESHOOTING.md`
- `_meta.json`
- `handle_event.js`
- `index.js`
- `package-lock.json`
- `package.json`
- `send.js`
- `send_persona.js`
- `send_safe.js`
- `test.js`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23