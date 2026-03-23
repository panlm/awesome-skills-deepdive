# Clawver Onboarding

> 设置新的 Clawver 商店——注册 Agent、配置 Stripe 支付、自定义店面，从零开始到接受付款的完整引导。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Clawver Onboarding |
| **作者** | nwang783 |
| **版本** | 1.4.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/nwang783-clawver-onboarding |

## 功能概述
- Agent 注册：通过 API 创建商店，设置名称、URL slug 和简介
- Stripe 支付接入：引导完成 Stripe 身份验证和支付配置（需人工参与）
- 店面自定义：配置商店外观和展示内容
- 创建首个产品：上架商品并设置定价
- 关联卖家账户：将 Agent 关联到已有卖家身份
- Bug 报告和产品反馈：内置向 Clawver 提交问题的流程

## 使用场景
- AI Agent 首次创建 Clawver 在线商店，完成从注册到收款的全流程
- 配置 Stripe 支付通道以接受客户付款
- 快速上架数字商品或 AI 生成内容到 Clawver 市场

## 依赖和前提条件
- 环境变量：`CLAW_API_KEY`（注册后获取，需立即保存）
- 网络访问：`https://api.clawver.store`
- Stripe 身份验证（需人工操作）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
