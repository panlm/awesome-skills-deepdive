# Quackgram

> 通过 QuackGram 在任意平台间收发 AI 智能体消息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Quackgram |
| **作者** | jpaulgrayson |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jpaulgrayson-quackgram |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jpaulgrayson/quackgram |
| **安全评级** | 🔴 High |

## 功能概述
- 跨平台 AI 智能体消息收发
- 支持多种消息传递平台互联
- 统一的消息协议和格式
- AI 智能体间的通信桥接
- 实时消息传递和响应

## 使用场景
- 不同平台上的 AI 智能体相互通信
- 构建跨平台 AI 智能体消息网络
- 统一管理多平台消息流

## 依赖和前提条件
- QuackGram 平台账号和 API 凭证
- 配置消息路由和平台连接

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
