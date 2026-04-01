# Snipeit Skill

> 集成 Snipe-IT 资产管理系统，自动化 IT 设备管理和审计

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Snipeit Skill |
| **作者** | bivex |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/bivex-snipeit-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bivex/snipeit-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 集成 Snipe-IT 资产管理系统
- 查询和管理 IT 硬件资产
- 跟踪设备分配和归还状态
- 生成资产报告和审计数据
- 支持资产标签和分类管理
- 适用于企业 IT 资产管理自动化

## 使用场景
- 通过 AI 助手查询和管理公司 IT 资产
- 自动化设备分配、归还和审计流程
- 生成资产管理报表和统计数据

## 依赖和前提条件
- Bash/Shell 环境
- API Key
- API Token
- 环境变量 `PATCH`

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
