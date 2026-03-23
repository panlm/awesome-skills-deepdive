# Airc

> IRC 聊天客户端，连接 IRC 服务器参与频道聊天，支持消息收发和频道管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Airc |
| **作者** | vortitron |
| **版本** | 0.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/vortitron-airc |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vortitron/airc |
| **安全评级** | 🔴 High |

## 功能概述
- 连接到指定 IRC 服务器和频道
- 发送和接收 IRC 频道消息
- 加入和退出 IRC 频道
- 监听频道活动和事件
- 支持多频道同时在线
- 私聊消息收发

## 使用场景
- 智能体加入 IRC 社区参与技术讨论
- 监控 IRC 频道获取实时信息和通知
- 通过 IRC 实现与其他系统或用户的通信

## 依赖和前提条件
- 目标 IRC 服务器地址和端口
- IRC 账号昵称（部分服务器需注册）
- 网络能访问 IRC 服务器

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `config.json`
- `irc.js`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
