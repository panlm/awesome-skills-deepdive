# Splitwise

> 费用分摊和账单拆分工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Splitwise |
| **作者** | richieforeman |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/richieforeman-splitwise |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/richieforeman/splitwise |
| **安全评级** | 🟡 Medium |

## 功能概述
- 多人费用智能分摊
- 账单拆分计算
- 支持多种分摊方式
- 结算金额自动计算

## 使用场景
- 团队聚餐后自动计算每人应付金额
- 旅行费用的公平分摊和结算

## 依赖和前提条件
- API 密钥
- Python 运行环境

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23