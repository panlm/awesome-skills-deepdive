# Workcrm

> CRM 工作流管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Workcrm |
| **作者** | extraterrest |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/extraterrest-workcrm |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/extraterrest/workcrm |
| **安全评级** | 🟢 Low |

## 功能概述
- CRM 客户关系管理
- 销售流程自动化
- 客户数据查询和更新
- 工作流触发和执行

## 使用场景
- 自动化 CRM 中的客户跟进和销售流程
- 通过 AI 助手管理和查询 CRM 客户数据

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `pyproject.toml`
- `tests`
- `workcrm`
- `workcrm.egg-info`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。Prompt 注入：存在可疑 Prompt 模式；信息采集：读取环境变量或系统信息




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23