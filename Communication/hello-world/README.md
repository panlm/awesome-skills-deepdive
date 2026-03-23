# Hello World

> 最基础的 OpenClaw skill 示例，返回简单的自定义问候消息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hello World |
| **作者** | mercuryeey |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/mercuryeey-hello-world |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mercuryeey/hello-world |
| **安全评级** | 🟢 Low |

## 功能概述
- 返回简单的问候消息
- 支持基本的自定义参数
- 代码结构简洁清晰，适合学习

## 使用场景
- OpenClaw skill 开发入门教程
- 验证 skill 安装和运行环境是否正常

## 依赖和前提条件
- OpenClaw 运行环境

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
