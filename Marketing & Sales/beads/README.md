# Beads Task Tracker

> 内容串珠工具，将碎片信息串联成完整叙事

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Beads Task Tracker |
| **作者** | rnijhara |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/rnijhara-beads |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rnijhara/beads |
| **安全评级** | 🟢 Low |

## 功能概述
- 碎片化内容聚合
- 信息串联和叙事构建
- 主题提取和归纳
- 结构化内容输出

## 使用场景
- 将分散的笔记和想法串联成完整的文章
- 从多个信息源提取主题构建统一叙事

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
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。越权操作：涉及权限相关操作；持久化机制：涉及定时或后台任务




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23