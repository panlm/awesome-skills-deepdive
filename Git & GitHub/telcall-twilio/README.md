# TelCall Twilio

> 通过 Twilio 语音 API 发起紧急电话呼叫，播放文字转语音消息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TelCall Twilio |
| **作者** | cnvipstar |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/cnvipstar-telcall-twilio |

## 功能概述
- 通过 Twilio Voice API 发起电话呼叫并播放 TTS 语音消息
- 支持多语言文字转语音（TwiML）
- 提供交互式配置脚本（setup.sh）设置 Twilio 凭证
- 简单的命令行调用方式（call.sh）
- 与 OpenClaw Agent 集成，支持自然语言触发（如"打电话给我：服务器挂了！"）
- 低成本运营：电话号码约 $1/月，通话约 $0.02-0.15/分钟

## 使用场景
- 服务器宕机、安全事件等紧急情况下自动电话告警通知
- AI Agent 监控到异常后通过电话呼叫值班人员
- 需要确保关键告警被及时接收的场景（比邮件和消息更紧急）

## 依赖和前提条件
- Twilio 账号（需绑定信用卡用于生产环境）
- 购买一个 Twilio 电话号码（具有 Voice 能力，约 $1/月）
- Twilio Account SID 和 Auth Token
- 试用账号需先验证目标号码，或升级账号（$20）解锁任意号码拨打
- `curl`、`jq`

## 安全状态
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
