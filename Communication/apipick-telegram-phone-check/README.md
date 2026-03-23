# Telegram Phone Checker

> 通过 APIPick API 检查指定手机号码是否已注册 Telegram 账号

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Telegram Phone Checker |
| **作者** | javainthinking |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/javainthinking-apipick-telegram-phone-check |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/javainthinking/apipick-telegram-phone-check |
| **安全评级** | 🔴 High |

## 功能概述
- 查询手机号的 Telegram 注册状态
- 批量号码检查支持
- 返回注册状态和基本账号信息
- API 调用简单快速

## 使用场景
- 验证联系人是否使用 Telegram 以选择通信渠道
- 用户注册流程中检测已有 Telegram 账号
- 社交平台用户验证和反欺诈场景

## 依赖和前提条件
- APIPick API 密钥
- 网络连接到 APIPick 服务

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

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
