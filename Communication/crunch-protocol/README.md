# Crunch Protocol

> Crunch Protocol CLI 的自然语言接口，将用户自然语言请求智能映射到对应的 CLI 命令并执行

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crunch Protocol |
| **作者** | philippwassibauer |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/philippwassibauer-crunch-protocol |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/philippwassibauer/crunch-protocol |
| **安全评级** | 🔴 High |

## 功能概述
- 自然语言解析用户意图并映射到 CLI 命令
- 支持 Crunch Protocol 全部 CLI 操作
- 自动补全命令参数和选项
- 交互式命令确认与执行
- 错误处理与友好提示

## 使用场景
- 不熟悉 CLI 语法时通过自然语言操作 Crunch Protocol
- 快速执行 Crunch Protocol 常用操作

## 依赖和前提条件
- 已安装 Crunch Protocol CLI
- OpenClaw 环境已配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
