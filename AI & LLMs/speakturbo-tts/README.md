# Speak Turbo - Talk to your Claude 90ms latency!

> 超低延迟语音合成服务，让 Claude 实现 90ms 实时语音对话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Speak Turbo - Talk to your Claude 90ms latency! |
| **作者** | emzod |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/emzod-speakturbo-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/emzod/speakturbo-tts |
| **安全评级** | 🟡 Medium |

## 功能概述
- 提供超低延迟（90ms）的语音合成服务
- 支持与 Claude 进行实时语音对话
- 使用 SpeakTurbo 引擎实现高速 TTS
- 支持多种语音风格和参数调节
- 适用于语音助手和实时交互场景
- 集成简便，开箱即用

## 使用场景
- 构建超低延迟的语音交互助手
- 为 Claude 对话添加实时语音输出能力
- 在实时场景中需要快速语音反馈时使用

## 依赖和前提条件
- Node.js 运行环境
- Python 运行环境
- Bash/Shell 环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive skill 自动生成
