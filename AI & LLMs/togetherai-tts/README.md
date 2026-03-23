# Togetherai Tts

> Text-to-speech using TogetherAI API with MiniMax speech-2.6-turbo model.

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
- `TOGETHERAI_API_KEY`: Your TogetherAI API key
- `TOGETHERAI_MODEL`: Model to use (default: minimax/speech-2.6-turbo)
- `TTS_FORMAT`: Output format (default: mp3)
- `TTS_VOICE`: Voice to use (default: default)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package.json`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23