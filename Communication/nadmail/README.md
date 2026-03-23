# Nadmail

> 基于 Monad 区块链的 AI 智能体专属邮箱，注册 yourname@nadmail.ai 地址收发邮件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Nadmail |
| **作者** | daaab |
| **版本** | 2.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/daaab-nadmail |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/daaab/nadmail |
| **安全评级** | 🔴 High |

## 功能概述
- 注册 @nadmail.ai 专属邮箱地址
- 基于 Monad 区块链的去中心化邮件服务
- AI 智能体独立收发电子邮件
- 邮件加密和身份验证
- 支持与标准邮箱互通
- 智能体间的链上通信

## 使用场景
- 为 AI 智能体创建专属邮箱用于自动化通信
- 智能体代表用户发送报告和通知邮件
- 区块链项目中智能体间的安全通信

## 依赖和前提条件
- Monad 区块链钱包地址
- NadMail 服务注册
- API 密钥配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
