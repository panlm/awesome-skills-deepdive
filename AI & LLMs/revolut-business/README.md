# Revolut Business

> 集成 Revolut Business API，自动化管理企业财务和多币种账户

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Revolut Business |
| **作者** | christianhaberl |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/christianhaberl-revolut-business |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/christianhaberl/revolut-business |
| **安全评级** | 🟡 Medium |

## 功能概述
- 集成 Revolut Business API 进行财务管理
- 查询账户余额和交易记录
- 管理多币种企业账户
- 自动化支付和转账操作
- 获取实时汇率信息
- 生成财务报告和数据分析

## 使用场景
- 自动化查询和管理企业多币种账户
- 通过 AI 助手完成日常财务操作和报告生成
- 集成到企业财务工作流实现支付自动化

## 依赖和前提条件
- Python 运行环境
- Bash/Shell 环境
- 环境变量 `AAAA`
- 环境变量 `REVOLUT_CLIENT_ID`
- 环境变量 `REVOLUT_ISS_DOMAIN`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
