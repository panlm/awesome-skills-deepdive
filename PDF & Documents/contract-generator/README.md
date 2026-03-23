# Contract Generator

> 智能合同文档生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Contract Generator |
| **作者** | seanwyngaard |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/seanwyngaard-contract-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seanwyngaard/contract-generator |
| **安全评级** | 🟢 Low |

## 功能概述
- 根据模板自动生成合同文档
- 支持多种合同类型（服务、租赁、采购等）
- 自定义合同条款和参数
- 输出为标准文档格式

## 使用场景
- 根据客户信息自动生成服务合同
- 批量创建标准化的租赁合同文档

## 依赖和前提条件
- AWS
- Stripe

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；持久化机制：涉及定时或后台任务




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23