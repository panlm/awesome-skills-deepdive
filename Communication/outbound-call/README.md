# Outbound Call

> 通过 ElevenLabs 语音智能体和 Twilio 拨打外呼电话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Outbound Call |
| **作者** | humanjesse |
| **版本** | 0.1.5 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/humanjesse-outbound-call |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/humanjesse/outbound-call |
| **安全评级** | 🟢 Low |

## 功能概述
- 使用 ElevenLabs 高质量语音合成拨打电话
- 通过 Twilio 电话网络发起外呼
- AI 语音智能体自动进行电话对话
- 支持自定义语音和对话脚本
- 实时语音交互与响应

## 使用场景
- 自动化客户通知和提醒电话
- AI 驱动的电话外呼与语音交互
- 预约确认和信息传达

## 依赖和前提条件
- ElevenLabs API 密钥
- Twilio 账号及电话号码
- 配置语音智能体参数

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `call.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
