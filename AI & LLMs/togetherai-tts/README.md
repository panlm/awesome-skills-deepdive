# Togetherai Tts

> 使用 Together AI 平台将文本转换为高质量语音

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Togetherai Tts |
| **作者** | marcus20232023 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/marcus20232023-togetherai-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/marcus20232023/togetherai-tts |
| **安全评级** | 🟡 Medium |

## 功能概述
- 使用 Together AI 的语音合成 API
- 将文本转换为高质量语音输出
- 支持多种语音模型和声音选择
- 提供低延迟的实时语音生成
- 集成 Together AI 平台的 TTS 能力
- 适用于语音助手和内容朗读场景

## 使用场景
- 将 AI 生成的文本内容转换为语音输出
- 构建语音助手应用集成 Together AI TTS
- 为内容创作自动生成配音和朗读音频

## 依赖和前提条件
- Node.js 运行环境
- Bash/Shell 环境
- API Key
- Together AI API Key
- 环境变量 `TOGETHERAI_API_KEY`
- 环境变量 `TOGETHERAI_MODEL`
- 环境变量 `TTS_FORMAT`
- 环境变量 `TTS_VOICE`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
