# unifi

> 通过本地网关 API 查询和监控 UniFi 网络

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | unifi |
| **作者** | jmagar |
| **ClawHub** | https://clawskills.sh/skills/jmagar-unifi |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jmagar/unifi |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出 UniFi 设备（AP、交换机、网关）状态和在线时间
- 显示已连接客户端（主机名、IP、信号、AP）
- 站点级网络健康概览（WAN/LAN/WLAN）
- DPI 流量分析（按应用排行）
- 近期告警和事件
- 所有操作均为只读安全

## 使用场景
- 监控家庭/办公网络设备状态
- 查看谁正在使用网络
- 排查网络问题

## 依赖和前提条件
- curl、jq
- UniFi OS 本地管理员账户
- 配置文件 `~/.clawdbot/credentials/unifi/config.json`

## 包含文件
- `SKILL.md` — 技能定义
- `scripts/unifi-api.sh` — API 辅助脚本（登录和认证请求）
- `scripts/dashboard.sh` — 综合仪表板
- `scripts/devices.sh` — 设备列表
- `scripts/clients.sh` — 客户端列表
- `scripts/health.sh` — 健康状态
- `scripts/top-apps.sh` — DPI 应用排行
- `scripts/alerts.sh` — 告警信息
- `references/unifi-readonly-endpoints.md` — 只读端点参考

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅 curl/jq HTTP 请求 |
| SEC-02 数据外泄 | 🟢 Safe | 从本地 UniFi 网关读取数据 |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.clawdbot/credentials/unifi/config.json（含用户名密码） |
| SEC-04 供应链风险 | 🟢 Safe | 纯 bash 脚本 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件（临时 cookie 文件除外） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅只读 GET 操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 获取网络设备和客户端信息（IP、MAC、信号等） |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 只读网络监控工具，但可获取详细网络拓扑和客户端信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
