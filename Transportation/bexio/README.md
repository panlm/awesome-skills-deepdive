# bexio

> 瑞士 Bexio 商业软件 API 集成，管理联系人、报价、发票和订单

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | bexio |
| **作者** | rdewolff |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/rdewolff-bexio |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rdewolff/bexio |
| **安全评级** | 🟡 Medium |

## 功能概述
- 管理客户和供应商联系人信息
- 创建和跟踪报价单/要约
- 生成发票并追踪付款状态
- 管理订单流程和库存
- 支持瑞士会计标准和税务要求

## 使用场景
- 为瑞士客户自动创建报价单并转换为发票
- 批量管理联系人信息并同步到 Bexio 系统
- 追踪未付发票并生成账龄报告

## 依赖和前提条件
- API Key（Bexio）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
