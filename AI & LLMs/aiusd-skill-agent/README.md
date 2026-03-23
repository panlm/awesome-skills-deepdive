# trade-with-aiusd

> AIUSD 加密货币交易技能，通过自然语言在 Telegram、Discord、WhatsApp 等平台进行加密货币交易和账户管理。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | trade-with-aiusd |
| **作者** | chaunceyliu |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/chaunceyliu-aiusd-skill-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chaunceyliu/aiusd-skill-agent |
| **安全评级** | 🔴 High |

## 功能概述
- 通过自然语言对话执行加密货币交易（买入/卖出）
- 查询 AIUSD 账户余额和交易历史
- 查看交易地址和账户详情
- 支持拖放安装，开箱即用
- 自动处理 OAuth 认证流程
- 兼容 Telegram、Discord、WhatsApp 等多平台

## 使用场景
- 在聊天中用自然语言下达交易指令，如"用 USDC 买入 100 美元的 SOL"
- 随时查询加密货币账户余额和近期交易记录
- 通过 AI 助手管理多平台上的加密货币操作

## 依赖和前提条件
- 需要 Node.js / npm
- 需要 AIUSD 账户和 OAuth 认证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
