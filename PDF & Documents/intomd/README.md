# Intomd

> 将各种格式内容转换为 Markdown

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Intomd |
| **作者** | rezhajulio |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/rezhajulio-intomd |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rezhajulio/intomd |
| **安全评级** | 🟢 Low |

## 功能概述
- 多种输入格式支持
- 转换为标准 Markdown 格式
- 保持文档结构和层级
- 支持批量转换处理

## 使用场景
- 将 HTML 页面内容转换为 Markdown 笔记
- 统一不同来源的文档为 Markdown 格式

## 依赖和前提条件
- 无特殊依赖

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
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23