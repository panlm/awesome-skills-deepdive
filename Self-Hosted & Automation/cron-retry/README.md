# cron-retry

> 网络恢复时自动重试失败的 cron 任务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | cron-retry |
| **作者** | jrbobbyhansen-pixel |
| **ClawHub** | https://clawskills.sh/skills/jrbobbyhansen-pixel-cron-retry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jrbobbyhansen-pixel/cron-retry |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过心跳检测因网络错误失败的 cron 任务
- 匹配已知网络错误模式（ETIMEDOUT、ECONNREFUSED 等）
- 仅重试瞬时网络错误，跳过逻辑/认证错误
- 自动集成 HEARTBEAT.md 工作流
- 安全防护：不创建重试循环

## 使用场景
- 网络不稳定时自动恢复失败的定时消息推送
- 连接恢复后重试失败的 API 调用任务

## 依赖和前提条件
- OpenClaw cron 系统
- HEARTBEAT.md 配置

## 包含文件
- `SKILL.md` — 技能定义和完整工作流说明
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅通过 cron tool API 列出和运行任务，无直接命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 不发送数据到外部 |
| SEC-03 凭证获取 | 🟢 Safe | 不处理凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 SKILL.md 指令，无代码依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无外部输入处理 |
| SEC-07 越权操作 | 🟢 Safe | 仅重试已有的 cron 任务 |
| SEC-08 持久化机制 | 🟢 Safe | 无新增持久化，仅操作已有 cron 任务 |
| SEC-09 信息采集 | 🟢 Safe | 仅检查 cron 任务状态 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯文本说明 |

**综合评级: 🟢 Low**
**风险摘要:** 纯指令型 skill，仅操作已有 cron 任务的重试逻辑，无代码无网络操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
