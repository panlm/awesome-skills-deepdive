# Accountsos

> 面向英国小微企业的 AI 原生会计工具，自动跟踪交易、发票和报税

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Accountsos |
| **作者** | paulgosnell |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/paulgosnell-accountsos |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/paulgosnell/accountsos |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动跟踪银行交易和费用分类
- 创建和管理发票、追踪付款状态
- 处理 VAT 申报和英国税务合规
- 自动对账和财务报表生成
- 支持 HMRC Making Tax Digital (MTD) 集成

## 使用场景
- 英国自由职业者自动分类银行交易并生成发票
- 季度 VAT 申报前自动汇总交易数据
- 追踪客户未付款项并发送催款提醒

## 依赖和前提条件
- API Key、Node.js / npm

## 安全状态
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
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
