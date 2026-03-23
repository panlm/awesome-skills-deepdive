# pidgesms

> 通过 Android 手机使用 Pidge 收发短信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | pidgesms |
| **作者** | typhonius |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/typhonius-pidgesms |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/typhonius/pidgesms |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 Android 设备收发短信
- 使用 Pidge 协议与手机通信
- AI 智能体代理短信读写操作
- 支持短信内容查看和回复
- 无需额外 SIM 卡或短信网关

## 使用场景
- 通过 AI 智能体远程收发短信
- 自动化短信通知和回复
- 利用现有 Android 手机作为短信网关

## 依赖和前提条件
- Android 手机安装 Pidge 应用
- 手机与 OpenClaw 网络连通
- 有效的 SIM 卡和短信服务

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
