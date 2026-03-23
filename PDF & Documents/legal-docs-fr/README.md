# Legal Docs FR

> 法语法律文档自动生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Legal Docs FR |
| **作者** | hugosbl |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/hugosbl-legal-docs-fr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hugosbl/legal-docs-fr |
| **安全评级** | 🟢 Low |

## 功能概述
- 生成标准法语法律文档
- 支持多种法律文书模板
- 合规性检查和验证
- 法律术语规范化处理

## 使用场景
- 为法语客户自动生成合规的法律合同
- 创建标准化的法语法律声明文档

## 依赖和前提条件
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。Prompt 注入：存在可疑 Prompt 模式




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23