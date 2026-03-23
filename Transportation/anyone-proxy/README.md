# Anyone Procotol Proxy

> 通过 Anyone 网络实现 IP 地址匿名和隐藏服务访问

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
- 通过 Anyone 匿名网络进行 IP 地址掩盖
- 访问 Anyone 网络上的隐藏服务
- 配置 SOCKS 代理进行匿名网络访问
- 支持匿名浏览和数据传输

## 使用场景
- 在进行安全研究时通过匿名网络访问目标
- 配置 Agent 使用匿名代理保护隐私

## 依赖和前提条件
- Anyone 网络客户端

## 安全状态
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

> 本文档由 awesome-skills-deepdive skill 自动生成
