# Beeper

> Beeper 聊天记录搜索和浏览工具，支持本地聊天历史的全文检索

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Beeper |
| **作者** | krausefx |
| **版本** | 0.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/krausefx-beeper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/krausefx/beeper |
| **安全评级** | 🟢 Low |

## 功能概述
- 搜索本地 Beeper 聊天记录
- 全文检索聊天内容
- 按联系人、日期等条件过滤
- 浏览和查看历史对话
- 聊天记录格式化展示

## 使用场景
- 快速查找 Beeper 中的历史聊天信息
- 根据关键词检索跨平台聊天内容
- 回顾特定联系人的历史对话记录

## 依赖和前提条件
- Beeper 桌面客户端已安装并登录
- 本地聊天数据库可访问

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖；Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
