# speedtest

> 使用 Ookla Speedtest CLI 测试网络速度并分享结果

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | speedtest |
| **作者** | spsneo |
| **ClawHub** | https://clawskills.sh/skills/spsneo-speedtest |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/spsneo/speedtest |
| **安全评级** | 🟢 Low |

## 功能概述
- 测量下载/上传速度、延迟和丢包
- 格式化输出适合社交分享
- 历史记录追踪速度趋势
- 交互式发布到 Moltbook/Twitter
- 状态指示器（优秀/良好/慢）

## 使用场景
- 诊断网络连接问题
- 定期监控网络速度
- 在社交平台分享基础设施数据

## 依赖和前提条件
- speedtest CLI（Ookla）
- bash、jq
- Moltbook API Key（可选，用于发布）

## 包含文件
- `SKILL.md — 使用指南`
- `scripts/speedtest-social.sh — 社交分享脚本`
- `scripts/speedtest-history.sh — 历史追踪脚本`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 speedtest CLI 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 可选发布速度结果到 Moltbook/Twitter |
| SEC-03 凭证获取 | 🟢 Safe | 仅可选的 Moltbook 凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖系统级 speedtest CLI |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 ~/.openclaw/data/speedtest-history.jsonl |
| SEC-06 Prompt 注入 | 🟢 Safe | CLI 工具层 |
| SEC-07 越权操作 | 🟢 Safe | 仅网络测速 |
| SEC-08 持久化机制 | 🟢 Safe | 按需运行 |
| SEC-09 信息采集 | 🟡 Medium | 收集网络性能数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本清晰透明 |

**综合评级: 🟢 Low**
**风险摘要:** 标准网络测速工具封装

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
