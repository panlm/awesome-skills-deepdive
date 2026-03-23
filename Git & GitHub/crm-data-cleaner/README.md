# CRM Data Cleaner

> CRM 数据清洗工具——对联系人和公司记录进行去重、规范化和数据富化，支持 HubSpot、Salesforce、Pipedrive 或任何支持 CSV 导出的 CRM 系统。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CRM Data Cleaner |
| **作者** | luigi08001 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/luigi08001-crm-data-cleaner |

## 功能概述
- 去重策略：识别和合并同一联系人/公司的多条记录（姓名拼写变体、不同邮箱等）
- 数据规范化：统一电话号码格式、邮箱格式、地址格式等
- 数据富化：通过 Clearbit 或 Apollo 等外部数据源补全缺失信息
- 多平台支持：HubSpot、Salesforce、Pipedrive 以及 CSV 导入/导出工作流
- 数据质量审计：生成数据质量报告，识别不完整和不一致的记录
- 纯指令型技能——无脚本或代码执行，所有操作通过 CRM 平台 API 或 CSV 工作流完成

## 使用场景
- 定期清洗 CRM 中的重复联系人和公司记录，提升数据质量
- 批量规范化电话号码、邮箱等字段格式
- 通过 Clearbit/Apollo 等服务自动富化联系人信息，填补缺失数据

## 依赖和前提条件
- 环境变量：`HUBSPOT_ACCESS_TOKEN`（HubSpot 用户必需）
- 环境变量：`CLEARBIT_API_KEY` 或 `APOLLO_API_KEY`（数据富化可选）
- 环境变量：`SALESFORCE_ACCESS_TOKEN`（Salesforce 用户可选）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
