# Sovereign Daily Digest

> 每日信息摘要自动生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sovereign Daily Digest |
| **作者** | ryudi84 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ryudi84-sovereign-daily-digest |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryudi84/sovereign-daily-digest |
| **安全评级** | 🔴 High |

## 功能概述
- 自动收集和汇总每日信息
- 多源内容聚合
- 智能摘要生成
- 定制化信息过滤

## 使用场景
- 每日自动生成行业新闻和信息摘要
- 个性化定制每日信息简报

## 依赖和前提条件
- Python 运行环境
- OpenAI API
- Google API
- GitHub API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23