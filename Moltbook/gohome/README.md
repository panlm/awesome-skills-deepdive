# gohome

> 通过 gRPC 发现和操控 GoHome 智能家居系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gohome |
| **作者** | local |
| **ClawHub** | https://clawskills.sh/skills/local-gohome |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/local/gohome |
| **安全评级** | 🟡 Medium |

## 功能概述
- gRPC 服务发现和插件检查
- RPC 方法列表和调用
- Roborock 和 Tado 设备管理
- Metrics 监控和 Grafana 集成
- 写操作需人工批准

## 使用场景
- 监控和操控 GoHome 智能家居设备
- 检查智能家居服务状态和指标

## 依赖和前提条件
- GoHome 服务实例
- gohome-cli
- GOHOME_GRPC_ADDR 和 GOHOME_HTTP_BASE 环境变量

## 包含文件
- `SKILL.md — gRPC 操作指南`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 gohome-cli 和 curl 执行系统命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与本地 GoHome 服务通信 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 GoHome 服务端点配置 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖本地安装的 gohome-cli |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件修改 |
| SEC-06 Prompt 注入 | 🟢 Safe | 硬件控制层 |
| SEC-07 越权操作 | 🟡 Medium | 可调用 RPC 方法控制智能家居设备 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取智能家居 Metrics 数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | SKILL.md 简洁透明 |

**综合评级: 🟡 Medium**
**风险摘要:** 可控制物联网设备，写操作需人工批准是好的安全设计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
