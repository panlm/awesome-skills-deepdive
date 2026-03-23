# ClawConnect

> 通用账户连接器，统一接口发推文、读写邮件、管理日历等多种在线服务操作

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ClawConnect |
| **作者** | yiweil |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/yiweil-clawconnect |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yiweil/clawconnect |
| **安全评级** | 🔴 High |

## 功能概述
- 统一接口管理多个在线服务账户
- 发布和管理 Twitter/X 推文
- 读取和发送电子邮件
- 日历事件的创建和管理
- OAuth 认证流程自动化
- 支持多种社交媒体和办公平台

## 使用场景
- 智能体通过统一接口管理用户的社交媒体和邮件
- 自动化日常办公流程：发邮件、更新日历、发推文
- 个人助理一站式处理跨平台的通信和日程任务

## 依赖和前提条件
- 配置目标服务的 OAuth 认证
- 授权智能体访问对应账户
- 安装 ClawConnect 插件

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
