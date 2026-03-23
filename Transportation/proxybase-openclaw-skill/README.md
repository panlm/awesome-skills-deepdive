# ProxyBase

> 通过 ProxyBase API 使用加密货币购买和管理 SOCKS5 住宅代理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ProxyBase |
| **作者** | proxybase-user |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/proxybase-user-proxybase-openclaw-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/proxybase-user/proxybase-openclaw-skill |
| **安全评级** | 🔴 High |

## 功能概述
- 购买 SOCKS5 住宅 IP 代理
- 支持加密货币支付（BTC、ETH 等）
- 管理代理 IP 池和轮换策略
- 查看代理使用量和状态

## 使用场景
- 为数据采集任务购买和配置住宅代理 IP
- 管理大规模代理 IP 池的轮换和可用性

## 依赖和前提条件
- API Key（ProxyBase）、加密钱包

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
