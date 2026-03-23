# Claw Me Maybe - Beeper Desktop API & Multi-Platform Messaging

> Beeper 全平台消息集成工具，跨 WhatsApp、iMessage、Signal、Telegram 等平台统一收发消息和搜索聊天记录

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Claw Me Maybe - Beeper Desktop API & Multi-Platform Messaging |
| **作者** | nickhamze |
| **版本** | 1.2.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/nickhamze-claw-me-maybe |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nickhamze/claw-me-maybe |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 Beeper 统一接口跨平台发送消息
- 支持 WhatsApp、iMessage、Signal、Telegram 等主流平台
- 跨平台聊天记录搜索和检索
- 统一管理多平台消息通知
- 自动消息路由和转发
- 联系人跨平台统一管理

## 使用场景
- 智能体通过单一接口在多个即时通讯平台上代发消息
- 统一搜索所有平台的聊天历史快速定位关键信息
- 助理智能体代用户管理和回复多平台消息

## 依赖和前提条件
- 拥有 Beeper 账户并登录目标平台
- 配置 Beeper API 访问权限
- 目标平台账户已在 Beeper 中关联

## 包含文件
- `README.md`
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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
