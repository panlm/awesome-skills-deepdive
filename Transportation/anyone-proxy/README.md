# Anyone Procotol Proxy

> This skill enables IP address masking and accessing hidden services on the Anyone Network. Route requests through the Anyone Protocol VPN network using a local SOCKS5 proxy.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Anyone Procotol Proxy |
| **作者** | ra3ka |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/ra3ka-anyone-proxy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ra3ka/anyone-proxy |
| **安全评级** | 🟡 Medium |

## 功能概述
- "@anyone-protocol/anyone-client"
- First connection may take up to 30 seconds while circuits are established
- The proxy persists across requests once started

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23