# Communication Skill

> 通用通信技能工具，为智能体提供基础的消息通信和交互能力

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Communication Skill |
| **作者** | aatmaan1 |
| **版本** | 0.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/aatmaan1-communication-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aatmaan1/communication-skill |
| **安全评级** | 🟢 Low |

## 功能概述
- 基础消息发送和接收功能
- 多渠道通信支持
- 消息格式化和模板管理
- 通信日志记录和查询

## 使用场景
- 作为其他通信类 skill 的基础依赖提供底层通信能力
- 简单场景下的消息发送和接收

## 依赖和前提条件
- OpenClaw 基础环境已配置
- 配置至少一个通信渠道

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
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
