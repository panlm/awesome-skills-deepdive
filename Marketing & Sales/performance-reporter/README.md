# Performance Reporter

> 绩效报告自动生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Performance Reporter |
| **作者** | aaron-he-zhu |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/aaron-he-zhu-performance-reporter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aaron-he-zhu/performance-reporter |
| **安全评级** | 🟡 Medium |

## 功能概述
- 绩效数据自动收集
- 多维度绩效分析
- 报告模板管理
- 趋势对比分析

## 使用场景
- 自动生成团队或项目的绩效分析报告
- 追踪关键绩效指标并生成趋势报告

## 依赖和前提条件
- API 密钥

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23