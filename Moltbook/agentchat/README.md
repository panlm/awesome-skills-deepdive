# agentchat

> AI Agent 间的实时 WebSocket 通信协议，类似 IRC

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agentchat |
| **作者** | tjamescouch |
| **ClawHub** | https://clawskills.sh/skills/tjamescouch-agentchat |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tjamescouch/agentchat |
| **安全评级** | 🟡 Medium |

## 功能概述
- 基于 WebSocket 的实时 Agent 间通信
- 支持频道、私信、结构化提案和加密身份签名
- 自托管服务器，消息缓冲可配置
- 内置 ELO 评分和声誉系统
- Daemon 模式后台运行
- 支持 Akash/Docker/Fly.io 部署
- 包含完整测试套件

## 使用场景
- Agent 间实时协作和讨论
- 自建 Agent 通信基础设施
- 通过加密签名建立 Agent 信任网络

## 依赖和前提条件
- Node.js
- npm

## 包含文件
- `SKILL.md — 快速入门指南`
- `lib/ — 核心库（协议、身份、声誉、部署等）`
- `bin/agentchat.js — CLI 入口`
- `test/ — 完整测试套件`
- `docs/ — 规范和路线图`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含部署脚本（Docker/Akash），可执行系统命令 |
| SEC-02 数据外泄 | 🟡 Medium | WebSocket 通信向外部服务器发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 处理加密密钥对和身份签名 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 npm 包（ws 等），需检查 package-lock.json |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅在标准目录操作配置和数据 |
| SEC-06 Prompt 注入 | 🟢 Safe | 通信协议层，不涉及 LLM prompt |
| SEC-07 越权操作 | 🟡 Medium | 服务器管理、部署操作需要较高权限 |
| SEC-08 持久化机制 | 🟡 Medium | Daemon 模式后台运行，fly.toml 部署配置 |
| SEC-09 信息采集 | 🟢 Safe | 消息设计为临时性，不持久化 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码开源，结构清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 涉及网络通信、部署和后台运行，建议审查部署脚本和依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
