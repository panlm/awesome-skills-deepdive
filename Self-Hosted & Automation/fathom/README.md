# fathom

> 连接 Fathom AI 获取会议录音、转录和摘要

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | fathom |
| **作者** | stopmoclay |
| **ClawHub** | https://clawskills.sh/skills/stopmoclay-fathom |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/stopmoclay/fathom |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出最近的通话记录
- 获取通话完整转录文本
- 获取 AI 生成的通话摘要和行动项
- 搜索通话内容（按关键词、发言人、日期）
- 设置 Webhook 自动同步
- 支持 JSON 和文本输出

## 使用场景
- 回顾会议内容和行动项
- 按关键词搜索历史通话记录
- 设置 Webhook 自动接收新会议摘要

## 依赖和前提条件
- curl、jq
- Fathom API Key（从 developers.fathom.ai 获取）

## 包含文件
- `SKILL.md` — 技能定义
- `scripts/setup.sh` — 连接测试
- `scripts/list-calls.sh` — 列出通话
- `scripts/get-transcript.sh` — 获取转录
- `scripts/get-summary.sh` — 获取摘要
- `scripts/search-calls.sh` — 搜索通话
- `scripts/setup-webhook.sh` — 设置 Webhook
- `examples/config-snippet.json` — 配置示例

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl/jq 标准命令 |
| SEC-02 数据外泄 | 🟡 Medium | 可注册 Webhook 将数据推送到指定 URL |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.fathom_api_key 或 FATHOM_API_KEY 环境变量 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 bash 脚本，无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件系统 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | API 只读操作（除 Webhook 设置） |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可获取完整通话转录内容（可能含敏感信息） |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 访问第三方会议 API 获取可能包含敏感内容的通话数据

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
