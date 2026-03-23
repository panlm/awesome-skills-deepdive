# Send SMS text and bulk messages via TelTel.io API

> 通过 TelTel (teltel.io) REST API 发送短信，支持智能体自动化短信通信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Send SMS text and bulk messages via TelTel.io API |
| **作者** | teltel-call-center |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/teltel-call-center-teltel-send-sms-text-message |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teltel-call-center/teltel-send-sms-text-message |
| **安全评级** | 🔴 High |

## 功能概述
- 调用 TelTel REST API 发送短信
- 支持自定义发送号码和接收号码
- 支持多国号码和国际短信
- 短信发送状态回调和确认
- 模板化短信内容管理

## 使用场景
- 智能体需要通过短信发送通知或验证码
- 自动化客户沟通流程中的短信触达
- 紧急事件时通过短信通知相关人员

## 依赖和前提条件
- TelTel (teltel.io) 账户
- TelTel API 密钥
- 已验证的发送号码

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
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
