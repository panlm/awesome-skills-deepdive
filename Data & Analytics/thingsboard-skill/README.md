# thingsboard-skill

> 通过 REST API 管理 ThingsBoard IoT 设备、仪表盘和遥测数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | thingsboard-skill |
| **作者** | hoangnv170752 |
| **ClawHub** | https://clawskills.sh/skills/hoangnv170752-thingsboard-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hoangnv170752/thingsboard-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 设备管理（列出、创建、更新、删除）
- 仪表盘管理
- 遥测数据查询和发送
- 用户和权限管理
- JWT 令牌认证
- 支持多服务器配置

## 使用场景
- IoT 设备的日常管理和监控
- 遥测数据查询和分析
- ThingsBoard 平台自动化管理

## 依赖和前提条件
- `TB_URL`、`TB_USERNAME`、`TB_PASSWORD` 环境变量
- ThingsBoard 实例
- curl, jq

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，API 使用指南 |
| credentials.json | ⚠️ 默认凭证模板（含示例密码） |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 curl 和 jq |
| SEC-02 数据外泄 | 🟢 Safe | 仅与用户指定的 ThingsBoard 通信 |
| SEC-03 凭证获取 | 🟡 Medium | credentials.json 包含默认密码模板，环境变量传递账密 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟡 Medium | 支持 sysadmin 级别操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅管理用户自己的 IoT 设备 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** credentials.json 含默认密码模板，支持高权限操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
