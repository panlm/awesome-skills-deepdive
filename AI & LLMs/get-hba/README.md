# Get a clank.money Human Bitcoin Address

> 通过 clank.money 服务获取人类验证的比特币地址

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Get a clank.money Human Bitcoin Address |
| **作者** | matbalez |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/matbalez-get-hba |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matbalez/get-hba |
| **安全评级** | 🟡 Medium |

## 功能概述
- 连接 clank.money 平台获取经过人类验证的比特币地址
- 为 AI 代理提供安全的加密货币交易地址获取方式
- 支持地址验证和有效性检查
- 提供人类身份关联的比特币地址映射
- 支持 API 调用和命令行两种使用方式
- 确保地址来源可追溯和可信

## 使用场景
- AI 代理需要获取可信比特币地址进行交易操作
- 构建去中心化应用时需要人类验证的加密货币地址
- 自动化加密货币支付流程中的地址获取环节

## 依赖和前提条件
- OpenClaw 运行环境
- clank.money 账户

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
