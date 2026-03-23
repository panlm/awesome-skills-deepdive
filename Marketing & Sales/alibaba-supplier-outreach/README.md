# Alibaba Supplier Outreach

> 阿里巴巴供应商外联工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Alibaba Supplier Outreach |
| **作者** | blockchainhb |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/blockchainhb-alibaba-supplier-outreach |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/blockchainhb/alibaba-supplier-outreach |
| **安全评级** | 🟡 Medium |

## 功能概述
- 阿里巴巴供应商搜索和筛选
- 供应商批量联系管理
- 外联模板和自动化
- 供应商信息管理

## 使用场景
- 在阿里巴巴平台上批量搜索和联系潜在供应商
- 自动化供应商开发和沟通流程

## 依赖和前提条件
- Chrome 浏览器

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23