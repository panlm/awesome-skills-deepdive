# Agent Card Provisioning

> 为 AI Agent 按需配置虚拟支付卡，支持一次性或多次使用的限额卡

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Card Provisioning |
| **作者** | proxyhq |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/proxyhq-agent-card-provisioning |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/proxyhq/agent-card-provisioning |
| **安全评级** | 🟢 Low |

## 功能概述
- 按需创建一次性或限额虚拟支付卡
- 设置消费限额、有效期和商户类别限制
- 实时查看卡片交易和余额
- 支持自动关闭过期或超额卡片
- 与主流支付网络集成

## 使用场景
- AI Agent 自动为在线采购任务生成一次性支付卡
- 为订阅服务创建限额卡避免超额扣款
- 批量管理多个 Agent 的支付卡配额

## 依赖和前提条件
- API Key

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

> 本文档由 awesome-skills-deepdive skill 自动生成
