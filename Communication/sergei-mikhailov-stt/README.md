# Speech to Text (Yandex SpeechKit)

> 使用 Yandex SpeechKit 进行语音消息识别，采用可扩展架构设计

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Speech to Text (Yandex SpeechKit) |
| **作者** | bzsega |
| **版本** | 1.1.8 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/bzsega-sergei-mikhailov-stt |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bzsega/sergei-mikhailov-stt |
| **安全评级** | 🔴 High |

## 功能概述
- 基于 Yandex SpeechKit 的语音识别
- 支持语音消息转文字
- 可扩展的模块化架构设计
- 支持多种音频格式输入
- 高精度俄语和多语言识别

## 使用场景
- 自动转录语音消息为文字
- 俄语和多语言语音内容识别
- 为聊天机器人添加语音理解能力

## 依赖和前提条件
- Yandex SpeechKit API 密钥
- Yandex Cloud 账号
- 配置音频输入格式和语言参数

## 包含文件
- `CLAUDE.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `assets`
- `check.sh`
- `requirements.txt`
- `scripts`
- `setup.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
