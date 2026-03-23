# Free Mobile SMS

> 通过法国 Free Mobile 运营商 API 向用户手机发送短信通知

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Free Mobile SMS |
| **作者** | dclauzel |
| **版本** | 0.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/dclauzel-freemobile-sms |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/dclauzel/freemobile-sms |
| **安全评级** | 🔴 High |

## 功能概述
- 调用 Free Mobile SMS API 发送短信
- 支持自定义短信内容和格式
- 适用于自动化通知和告警场景
- 轻量级实现，无需第三方短信服务

## 使用场景
- 法国 Free Mobile 用户接收 AI 智能体的自动通知
- 系统异常或任务完成时通过短信即时告警

## 依赖和前提条件
- 法国 Free Mobile 手机号和账户
- Free Mobile API 用户标识和密钥
- OpenClaw 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
