# mcp-hass

> 通过 MCP 协议控制 Home Assistant 智能家居设备和查询状态

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mcp-hass |
| **作者** | al-one |
| **ClawHub** | https://clawskills.sh/skills/al-one-mcp-hass |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/al-one/mcp-hass |
| **安全评级** | 🟡 Medium |

## 功能概述
- 设备开关控制
- 灯光亮度和颜色调节
- 风扇转速控制
- 设备状态查询
- mcporter 集成配置
- 支持区域和域名过滤

## 使用场景
- 语音/文字控制智能家居设备
- 查询家居设备状态
- 自动化场景联动

## 依赖和前提条件
mcporter 或 npx, HASS_ACCESS_TOKEN, HASS_BASE_URL

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 mcporter 执行 MCP 调用 |
| SEC-02 数据外泄 | 🟡 Medium | 与 Home Assistant REST API 通信 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 HASS_ACCESS_TOKEN 长期令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 mcporter 或 npx |
| SEC-05 文件系统篡改 | 🟢 Safe | 无本地文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 可控制所有智能家居设备（开/关/调节） |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可查询所有设备状态和区域信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 配置清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 智能家居控制权限广泛，需确保 HA 令牌安全和设备权限合理

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
