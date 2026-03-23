# mmEasyVoice

> 简易语音合成和播放工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mmEasyVoice |
| **作者** | blue-coconut |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/blue-coconut-mm-easy-voice |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/blue-coconut/mm-easy-voice |
| **安全评级** | 🟡 Medium |

## 功能概述
- Python 3.8+
- MINIMAX_VOICE_API_KEY environment variable (required)
- FFmpeg (optional, for audio merging/conversion)
- Up to 10,000 characters per request
- For longer text, split into multiple requests and merge later
- Example: `"Hello<#1.5#>world"` = 1.5 second pause between words
- Range: 0.01 to 99.99 seconds
- All available system voices (male, female)

## 使用场景
- 快速生成语音播放内容
- 支持简单的文本转语音功能
- 集成多种语音引擎

## 依赖和前提条件
- Python / pip
- macOS
- Homebrew
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `check_environment.py`
- `mmvoice.py`
- `reference`
- `requirements.txt`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
