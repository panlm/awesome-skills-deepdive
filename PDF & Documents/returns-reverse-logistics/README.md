# Returns Reverse Logistics

> 退货和逆向物流管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Returns Reverse Logistics |
| **作者** | nocodemf |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/nocodemf-returns-reverse-logistics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nocodemf/returns-reverse-logistics |
| **安全评级** | 🟡 Medium |

## 功能概述
- 退货流程自动化管理
- 逆向物流追踪
- 退款状态管理
- 退货数据统计分析

## 使用场景
- 自动化处理电商退货退款流程
- 追踪和管理逆向物流全流程

## 依赖和前提条件
- GitHub API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `evals`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23