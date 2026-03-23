# Localsend

> 使用 LocalSend 协议在局域网内向附近设备发送和接收文件，无需互联网连接

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Localsend |
| **作者** | chordlini |
| **版本** | 3.4.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/chordlini-localsend |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chordlini/localsend |
| **安全评级** | 🔴 High |

## 功能概述
- 基于 LocalSend 协议的局域网文件传输
- 自动发现同一网络内的可用设备
- 支持发送和接收多种类型文件
- 无需互联网连接，完全本地化传输
- 跨平台设备间文件共享

## 使用场景
- 在同一 Wi-Fi 下快速向手机或平板传输文件
- 团队内部局域网文件分发，无需上传云端
- AI 智能体将生成的文件直接推送到用户设备

## 依赖和前提条件
- 目标设备需安装 LocalSend 客户端
- 发送端和接收端需在同一局域网内
- OpenClaw 运行环境需具备网络访问权限

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
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
