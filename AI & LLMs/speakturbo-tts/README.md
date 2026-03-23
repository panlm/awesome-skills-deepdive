# Speak Turbo - Talk to your Claude 90ms latency!

> Give your agent the ability to speak to you real-time. Talk to your Claude! Ultra-fast TTS, text-to-speech, voice synthesis, audio output with ~90ms latency. 8 built-in voices for instant voice responses. For voice cloning, use the speak skill.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Speak Turbo - Talk to your Claude 90ms latency! |
| **作者** | emzod |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/emzod-speakturbo-tts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/emzod/speakturbo-tts |
| **安全评级** | 🟡 Medium |

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm
- Python / pip
- macOS

## 包含文件
- `AGENTS.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `install.sh`
- `package.json`
- `pyproject.toml`
- `speakturbo`
- `speakturbo-cli`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23