# Agentic Calling

> 让 AI 代理通过 Twilio 自主拨打和接听电话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agentic Calling |
| **作者** | kellyclaudeai |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/kellyclaudeai-agentic-calling |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kellyclaudeai/agentic-calling |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 Twilio 实现 AI 代理自主拨打外呼电话
- 支持接收来电并进行智能应答
- 提供短信通知功能（SMS 发送）
- 可查询通话状态和历史记录
- 支持通过环境变量或配置文件管理 Twilio 凭证
- 提供可执行脚本快速发起通话、发送短信和状态查询

## 使用场景
- 让 AI 代理自动电话通知用户重要事项（如日程提醒、异常告警）
- 构建 AI 语音客服系统，自动接听和处理来电
- 在无法接通电话时自动发送短信作为备选通知方式

## 依赖和前提条件
- Twilio 账号及 API 凭证（Account SID、Auth Token）
- Twilio 电话号码（支持语音功能）
- Bash 环境（用于执行脚本）

## 安全状态
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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
