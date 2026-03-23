# sixel-email

> 智能体专用 1:1 邮件通道，限定只能与单一地址互发邮件，实现安全隔离通信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sixel-email |
| **作者** | sixel-et |
| **版本** | 1.0.6 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/sixel-et-sixel-email |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sixel-et/sixel-email |
| **安全评级** | 🔴 High |

## 功能概述
- 严格限制为单一发件/收件地址的 1:1 通信
- 智能体可自动发送和接收邮件
- 内置安全隔离机制防止邮件滥用
- 支持邮件内容的结构化解析
- 自动过滤非授权地址的邮件

## 使用场景
- 智能体与指定人员之间建立专属邮件沟通渠道
- 自动化工作流中需要邮件确认的安全通信场景
- 限制 AI 邮件权限范围以防止误发

## 依赖和前提条件
- 配置授权的邮件地址
- 邮件服务器 SMTP/IMAP 凭据
- Sixel 邮件服务账户

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
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
