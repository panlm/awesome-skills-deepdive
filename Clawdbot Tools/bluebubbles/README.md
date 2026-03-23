# bluebubbles

> 构建或更新 BlueBubbles iMessage 外部频道插件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | bluebubbles |
| **作者** | kevin19830331 |
| **ClawHub** | https://clawskills.sh/skills/kevin19830331-bluebubbles |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kevin19830331/bluebubbles |
| **安全评级** | 🟢 Low |

## 功能概述
- iMessage 消息收发集成
- Webhook 接收入站消息
- REST API 发送/探测
- 表情回应（tapback）支持
- 附件/贴纸下载
- 聊天已读标记

## 使用场景
- 通过 BlueBubbles 实现 Clawdbot 与 iMessage 互通
- 开发和维护 BlueBubbles 频道插件

## 依赖和前提条件
BlueBubbles 服务器（需运行在 macOS 上）

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯开发指导文档，无可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 涉及 HTTP webhook 和 REST API 通信 |
| SEC-03 凭证获取 | 🟡 Medium | 引用 serverUrl 和 password 配置 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖 Clawdbot 插件 SDK |
| SEC-05 文件系统篡改 | 🟢 Safe | 无直接文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 权限由 Clawdbot 频道系统控制 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 可访问 iMessage 聊天内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 开发文档类 skill，实际风险取决于 BlueBubbles 服务器配置

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
