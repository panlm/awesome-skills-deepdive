# Blinko

> 在 Abstract 链上无头运行 Blinko（链上弹珠台游戏），支持玩游戏、查看统计数据、排行榜和蜂蜜奖励追踪。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Blinko |
| **作者** | tolibear |
| **版本** | 1.1.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tolibear-blinko |

## 功能概述
- 完整的 commit-reveal 游戏流程：API 认证、链上游戏创建、模拟和结算
- 支持普通模式和困难模式（Hard mode: 0% 主游戏 RTP，需触发奖励才能获胜）
- 支持 V2 算法和配置
- 查看个人资料、游戏历史、排行榜和蜂蜜余额
- 下注范围 0.0001 - 0.1 ETH，10 个球通过 8 行钉子
- 支持 JSON 格式输出，方便程序化集成

## 使用场景
- AI Agent 自主在 Abstract 链上参与 Blinko 弹珠台游戏
- 查询游戏统计数据和链上排行榜
- 追踪蜂蜜奖励余额

## 依赖和前提条件
- Node.js / npm
- 环境变量：`WALLET_PRIVATE_KEY`（专用热钱包的私钥）
- Abstract 链上需有 ETH 用于 Gas 费和下注

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
