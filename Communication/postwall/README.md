# Postwall

> AI 智能体安全邮件网关，所有邮件读写操作需人工审批

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Postwall |
| **作者** | casperaiassist |
| **版本** | 1.7.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/casperaiassist-postwall |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/casperaiassist/postwall |
| **安全评级** | 🔴 High |

## 功能概述
- 为 AI 智能体提供安全的邮件访问通道
- 所有邮件操作需经人工审批确认
- 防止 AI 未经授权发送邮件
- 支持邮件读取和草稿创建
- 审批日志和操作记录追踪
- 可配置审批规则和白名单

## 使用场景
- 安全地让 AI 智能体处理邮件事务
- 企业环境中 AI 邮件操作的合规管控
- 防止 AI 误发或滥发邮件

## 依赖和前提条件
- 配置邮件服务器连接信息
- 设置审批流程和通知渠道
- 邮件账号授权

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
