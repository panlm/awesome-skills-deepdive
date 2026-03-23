# Signet Guardian

> AI Agent 支付守护中间件——在任何技能发起支付前进行安全检查和审批

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Signet Guardian |
| **作者** | rafalzacher1 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/rafalzacher1-signet-guardian |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rafalzacher1/signet-guardian |
| **安全评级** | 🟡 Medium |

## 功能概述
- 拦截和审查 Agent 发起的支付请求
- 实施支付金额限制和频率控制
- 多级审批流程管理
- 支付行为审计和日志记录

## 使用场景
- Agent 自动购物时通过守护中间件确保金额合理
- 设置每日支付限额防止异常消费

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

> 本文档由 awesome-skills-deepdive skill 自动生成
