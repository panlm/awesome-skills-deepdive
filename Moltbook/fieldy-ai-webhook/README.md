# fieldy-ai-webhook

> 将 Fieldy 语音转写 Webhook 集成到 Moltbot

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | fieldy-ai-webhook |
| **作者** | mrzilvis |
| **ClawHub** | https://clawskills.sh/skills/mrzilvis-fieldy-ai-webhook |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mrzilvis/fieldy-ai-webhook |
| **安全评级** | 🟢 Low |

## 功能概述
- Webhook 接收 Fieldy 语音转写数据
- Wake word 检测（Hey Fieldy）
- 转写内容记录到 JSONL 日志
- 与 Moltbot Gateway hooks 系统集成
- 可自定义唤醒词和解析逻辑

## 使用场景
- 将 Fieldy 语音助手与 Moltbot 集成
- 语音命令触发 Agent 任务
- 转写内容的自动归档

## 依赖和前提条件
- Node.js
- Moltbot Gateway（hooks 已启用）
- Fieldy 应用

## 包含文件
- `SKILL.md — 配置指南`
- `src/fieldy-webhook.js — Webhook 转换模块`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | JavaScript 模块仅做数据转换 |
| SEC-02 数据外泄 | 🟢 Safe | 数据仅写入本地 JSONL 文件 |
| SEC-03 凭证获取 | 🟡 Medium | 涉及 hooks.token 配置 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部 npm 依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 在 workspace/fieldy/transcripts/ 创建和写入日志文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 不涉及 LLM prompt |
| SEC-07 越权操作 | 🟢 Safe | 仅处理 Webhook 数据 |
| SEC-08 持久化机制 | 🟡 Medium | Webhook 端点持续监听 |
| SEC-09 信息采集 | 🟡 Medium | 记录语音转写内容到日志 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 简单的 Webhook 转换模块，行为透明

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
