# LNemail

> 基于比特币闪电网络的匿名邮箱服务，在 LNemail.net 上创建和使用加密邮箱

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LNemail |
| **作者** | lnemail |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/lnemail-lnemail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lnemail/lnemail |
| **安全评级** | 🔴 High |

## 功能概述
- 通过闪电网络支付创建匿名邮箱
- 在 LNemail.net 上收发加密邮件
- 无需个人信息即可注册使用
- 支持比特币闪电网络微支付
- 保护用户通信隐私和匿名性

## 使用场景
- 需要匿名通信的用户创建不可追踪的邮箱
- 使用比特币闪电网络进行隐私保护通信
- 注册需要邮箱但不想暴露真实身份的服务

## 依赖和前提条件
- 比特币闪电网络钱包
- 少量比特币用于支付邮箱服务
- OpenClaw 运行环境

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
