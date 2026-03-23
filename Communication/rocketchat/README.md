# RocketChat

> Rocket.Chat 团队消息平台集成 — 管理频道、消息、用户和集成（REST API）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | RocketChat |
| **作者** | zenjabba |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/zenjabba-rocketchat |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zenjabba/rocketchat |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 REST API 管理 Rocket.Chat 频道
- 发送、读取和搜索聊天消息
- 管理用户和权限设置
- 配置 Webhook 和第三方集成
- 频道创建、归档和管理操作
- 支持私聊和群组消息

## 使用场景
- AI 智能体自动发送团队通知和消息
- 自动化 Rocket.Chat 频道管理
- 跨系统消息集成和转发

## 依赖和前提条件
- Rocket.Chat 服务器地址和管理凭证
- API 用户令牌和权限配置
- Rocket.Chat 实例运行中

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
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
