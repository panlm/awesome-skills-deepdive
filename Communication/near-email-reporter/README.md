# Near Email Reporter

> 通过 SMTP 配置自动发送 NEAR 区块链相关报告和警报邮件，支持定时任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Near Email Reporter |
| **作者** | shaiss |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/shaiss-near-email-reporter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/shaiss/near-email-reporter |
| **安全评级** | 🔴 High |

## 功能概述
- NEAR 区块链数据报告邮件发送
- SMTP 邮件服务配置和管理
- 定时自动发送报告邮件
- 自定义报告模板和内容
- 异常警报邮件即时推送
- 支持多收件人和邮件列表

## 使用场景
- 每日自动发送 NEAR 账户资产变动报告
- NEAR 链上异常交易的实时邮件警报
- 定期向团队发送区块链项目运营报告

## 依赖和前提条件
- SMTP 邮件服务器配置（地址、端口、认证）
- NEAR 区块链节点或 API 访问
- 发件人邮箱账户

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
