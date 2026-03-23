# Key Expiry Tracker

> API 密钥、客户端密钥和证书的到期日期追踪器，防止凭据意外过期

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Key Expiry Tracker |
| **作者** | tradmangh |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/tradmangh-key-expiry-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tradmangh/key-expiry-tracker |
| **安全评级** | 🔴 High |

## 功能概述
- 追踪 API 密钥的到期时间
- 监控客户端密钥和证书有效期
- 到期前自动提醒和告警
- 集中管理所有凭据的到期元数据
- 支持自定义提前提醒天数

## 使用场景
- 企业 IT 团队统一管理各类证书和密钥的生命周期
- 在 API 密钥即将过期前收到提醒以避免服务中断
- 定期审计所有凭据的有效状态

## 依赖和前提条件
- 需要追踪的密钥/证书信息
- 告警通知渠道配置
- OpenClaw 运行环境

## 包含文件
- `METADATA.json`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
