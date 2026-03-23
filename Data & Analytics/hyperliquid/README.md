# hyperliquid

> 只读 Hyperliquid 加密货币市场数据助手（永续合约 + 现货）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | hyperliquid |
| **作者** | k0nkupa |
| **ClawHub** | https://clawskills.sh/skills/k0nkupa-hyperliquid |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/k0nkupa/hyperliquid |
| **安全评级** | 🟢 Low |

## 功能概述
- 实时报价：标记价/中间价/Oracle 价、24h 涨跌幅、交易量
- 24h 涨跌排行榜
- 资金费率排名
- L2 订单簿深度
- K 线图数据
- 只读账户查看（持仓、余额、订单、成交记录）
- 支持账户别名管理

## 使用场景
- 加密货币市场行情监控
- Hyperliquid 账户持仓查看
- 资金费率套利研究

## 依赖和前提条件
- Node.js ≥18

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| ORIGINAL_README.md | 原始说明 |
| references/hyperliquid-api.md | API 参考 |
| scripts/hyperliquid_api.mjs | API 客户端 |
| scripts/hyperliquid_chat.mjs | 聊天交互脚本 |
| scripts/hyperliquid_config.mjs | 配置管理 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 脚本，无 shell 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 Hyperliquid 官方 API 通信 |
| SEC-03 凭证获取 | 🟢 Safe | 无私钥操作，只读 API 不需要密钥 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部 npm 依赖，使用 Node.js 内置 fetch |
| SEC-05 文件系统篡改 | 🟡 Medium | 配置存储在 ~/.clawdbot/hyperliquid/config.json |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 严格只读，无交易功能 |
| SEC-08 持久化机制 | 🟡 Medium | 账户别名持久化到本地 config.json |
| SEC-09 信息采集 | 🟢 Safe | 仅获取公开市场数据和用户指定账户 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的只读加密市场数据工具，无私钥或交易操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
