# Crunch Protocol Skill

> Crunch Protocol CLI 的自然语言接口（替代 slug），功能与 crunch-protocol 相同

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crunch Protocol Skill |
| **作者** | philippwassibauer |
| **版本** | 0.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/philippwassibauer-crunch-protocol-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/philippwassibauer/crunch-protocol-skill |
| **安全评级** | 🔴 High |

## 功能概述
- 自然语言到 CLI 命令的智能映射
- 支持完整的 Crunch Protocol 命令集
- 命令参数自动推断与填充
- 执行结果格式化输出
- 上下文感知的命令建议

## 使用场景
- 通过对话方式操作 Crunch Protocol
- 团队成员快速上手 Crunch Protocol CLI

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
