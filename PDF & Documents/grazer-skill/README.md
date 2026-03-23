# Grazer

> 内容浏览和采集技能组件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Grazer |
| **作者** | scottcjn |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/scottcjn-grazer-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/scottcjn/grazer-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 网页内容浏览和采集
- 智能内容提取
- 多源信息聚合
- 结构化数据输出

## 使用场景
- 集成到工作流中自动采集网页内容
- 定期浏览和收集特定来源的信息

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Node.js
- Python pip
- npm
- AWS
- GitHub API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23