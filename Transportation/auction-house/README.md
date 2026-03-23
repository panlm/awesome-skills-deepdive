# House Auction

> 在 House 加密拍卖平台上搜寻、监控和出价竞拍

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | House Auction |
| **作者** | im-still-thinking |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/im-still-thinking-auction-house |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/im-still-thinking/auction-house |
| **安全评级** | 🟡 Medium |

## 功能概述
- 搜索和浏览 House 平台上的拍卖项目
- 实时监控拍卖状态和价格变化
- 自动出价和竞价策略管理
- 追踪拍卖历史和成交记录
- 支持加密货币支付和结算

## 使用场景
- 监控感兴趣的 NFT 拍卖并在合适价格自动出价
- 追踪特定类别拍卖品的历史成交价格趋势

## 依赖和前提条件
- API Key、加密钱包

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
