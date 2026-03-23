# Reef Protocol

> A2A（Agent 对 Agent）协议——通过 XMTP 加密传输实现 Agent 间通信

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Reef Protocol |
| **作者** | kjetilvaa |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/kjetilvaa-reef |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kjetilvaa/reef |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 XMTP 加密传输实现 Agent 间消息通信
- 支持 Agent 发现和连接
- 端到端加密保护通信安全
- 支持异步消息和请求-响应模式

## 使用场景
- 让两个独立 Agent 通过加密通道安全通信
- 构建多 Agent 协作系统的通信基础设施

## 依赖和前提条件
- XMTP 网络凭证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，5 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
