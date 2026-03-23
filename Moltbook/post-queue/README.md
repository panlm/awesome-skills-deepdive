# post-queue

> 帖子排队系统 — 处理限速平台的发帖冷却时间

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | post-queue |
| **作者** | luluf0x |
| **ClawHub** | https://clawskills.sh/skills/luluf0x-post-queue |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/luluf0x/post-queue |
| **安全评级** | 🟢 Low |

## 功能概述
- 添加帖子到队列
- 检查队列状态
- 冷却时间到期后自动处理
- 支持 Moltbook 等限速平台
- 本地 JSON 文件存储

## 使用场景
- 处理 Moltbook 的 30 分钟发帖限制
- 批量安排帖子发布

## 依赖和前提条件
- bash、jq、curl
- Moltbook API Key

## 包含文件
- `SKILL.md — 使用指南`
- `queue.sh — 队列管理脚本`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Shell 脚本通过 curl 发布帖子 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Moltbook 发送帖子 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.config/moltbook/credentials.json |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 bash/jq/curl |
| SEC-05 文件系统篡改 | 🟡 Medium | 在 ~/.local/share/post-queue/ 创建队列文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 不涉及 LLM |
| SEC-07 越权操作 | 🟢 Safe | 标准帖子发布 |
| SEC-08 持久化机制 | 🟡 Medium | 队列数据持久化到文件 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本清晰简洁 |

**综合评级: 🟢 Low**
**风险摘要:** 简单的帖子排队工具

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
