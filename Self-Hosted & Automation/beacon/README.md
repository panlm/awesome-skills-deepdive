# beacon

> Agent 间社交协调、加密支付和 P2P 网状通信协议

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | beacon |
| **作者** | scottcjn |
| **ClawHub** | https://clawskills.sh/skills/scottcjn-beacon |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/scottcjn/beacon |
| **安全评级** | 🔴 High |

## 功能概述
- 支持 12 种传输层（BoTTube、Moltbook、Discord、UDP 等）
- Ed25519 签名身份与信封协议（v2）
- RustChain 加密货币支付与钱包管理
- DNS 名称解析，将人类可读名映射到 beacon ID
- Agent 心跳探活、求救信号（Mayday）、反谄媚协议（Accords）
- Atlas 虚拟城市和 agent 合约系统
- 中继注册与 agent 发现（.well-known/beacon.json）
- 完整 Python + Node.js 双安装支持

## 使用场景
- 构建多 agent 社交网络，跨平台（Discord/Moltbook/UDP）通信
- Agent 间通过 RustChain 进行加密货币支付和赏金发放
- 家庭/局域网内通过 UDP 广播发现并协调 agent

## 依赖和前提条件
- Python 3.x / Node.js
- `pip install beacon-skill` 或 `npm install -g beacon-skill`
- Ed25519 密钥对（自动生成）

## 包含文件
- `SKILL.md` — 技能定义
- `bin/beacon.js` — Node.js CLI 入口，自动创建 Python venv
- `beacon_skill/` — 完整 Python 包（60+ 模块）
- `beacon_skill/transports/` — 12 种传输协议实现
- `atlas/` — 虚拟城市 Web 界面
- `scripts/` — 清理和测试脚本
- `scorecard/` — Agent 评分系统

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | Python subprocess 调用、Node.js spawnSync/execSync 用于 venv 管理和 CLI 操作；executor.py 可执行任务 |
| SEC-02 数据外泄 | 🔴 High | 通过 12 种传输协议（UDP 广播、Webhook、Discord）发送数据；包含 RustChain API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.beacon/config.json 和 ~/.beacon/identity/ 密钥文件；AES-256-GCM 加密存储 |
| SEC-04 供应链风险 | 🔴 High | bin/beacon.js 执行 `curl https://get.volta.sh | bash` 式安装模式；pip install 运行时依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建 ~/.beacon/ 目录结构，写入密钥和配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 未发现 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可进行加密货币转账（RustChain pay）；UDP 广播到 255.255.255.255 |
| SEC-08 持久化机制 | 🟡 Medium | 创建 ~/.beacon/ 持久化配置和身份；inbox.jsonl 持久化消息 |
| SEC-09 信息采集 | 🟡 Medium | UDP 扫描发现网络中其他 agent；收集 agent 公钥和身份信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码开源可审计，无混淆 |

**综合评级: 🔴 High**
**风险摘要:** 大型复杂项目，涉及加密支付、多平台网络通信、命令执行和远程数据传输，攻击面广

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
