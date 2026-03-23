# moltbot-ha

> 通过 Home Assistant REST API 控制智能家居设备

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbot-ha |
| **作者** | iamvaleriofantozzi |
| **ClawHub** | https://clawskills.sh/skills/iamvaleriofantozzi-moltbot-ha |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iamvaleriofantozzi/moltbot-ha |
| **安全评级** | 🟡 Medium |

## 功能概述
- 控制灯光、开关、窗帘、场景和气候
- 3 级安全系统（关键操作需确认）
- Agent 友好的错误消息和确认工作流
- 灵活的白名单/黑名单配置
- 支持表格和 JSON 输出格式
- 交互式和非交互式配置

## 使用场景
- 通过 Agent 控制智能家居设备
- 安全的 Home Assistant 远程操作

## 依赖和前提条件
- Python 3.10+
- Home Assistant 实例
- HA_TOKEN 长期访问令牌

## 包含文件
- `SKILL.md — 使用指南`
- `ORIGINAL_README.md — 详细说明`
- `CHANGELOG.md — 变更记录`
- `config.example.toml — 示例配置`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | CLI 工具调用 Home Assistant REST API |
| SEC-02 数据外泄 | 🟢 Safe | 仅与本地 HA 实例通信 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 HA_TOKEN 长期访问令牌 |
| SEC-04 供应链风险 | 🟡 Medium | Python 包（pip/uv 安装） |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | CLI 工具层 |
| SEC-07 越权操作 | 🟡 Medium | 可控制门锁、警报等关键设备 |
| SEC-08 持久化机制 | 🟢 Safe | 按需运行 |
| SEC-09 信息采集 | 🟡 Medium | 读取智能家居设备状态 |
| SEC-10 混淆/反分析 | 🟢 Safe | 开源代码，MIT 许可 |

**综合评级: 🟡 Medium**
**风险摘要:** 智能家居控制需要安全保障，3 级安全系统是好的设计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
