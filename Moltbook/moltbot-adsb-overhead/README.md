# moltbot-adsb-overhead

> 当飞机飞过头顶时发送 WhatsApp 通知（基于 ADS-B 数据）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | moltbot-adsb-overhead |
| **作者** | davestarling |
| **ClawHub** | https://clawskills.sh/skills/davestarling-moltbot-adsb-overhead |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/davestarling/moltbot-adsb-overhead |
| **安全评级** | 🟢 Low |

## 功能概述
- 连接本地 ADS-B SBS/BaseStation TCP 数据流
- 基于经纬度和半径检测头顶飞机
- 可选 tar1090 元数据丰富
- Planespotters 照片 API 集成
- Zero-AI 零模型调用通知器
- 冷却时间和持久状态避免重复通知
- 通过 WhatsApp 发送通知

## 使用场景
- 航空爱好者实时飞机监控
- 基于地理位置的飞机通知系统

## 依赖和前提条件
- Python 3
- ADS-B 接收器（SBS 端口 30003）
- Clawdbot/Moltbot（WhatsApp 配置）

## 包含文件
- `SKILL.md — 技能定义`
- `ORIGINAL_README.md — 详细说明`
- `scripts/sbs_overhead_check.py — SBS 数据采集和检测`
- `scripts/adsb_overhead_notify.py — WhatsApp 通知器`
- `scripts/adsb_config.py — 配置管理`
- `config.example.json — 示例配置`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | adsb_overhead_notify.py 调用 clawdbot message send 命令 |
| SEC-02 数据外泄 | 🟡 Medium | 通过 WhatsApp 发送飞机信息 |
| SEC-03 凭证获取 | 🟢 Safe | 配置存储在本地 JSON 文件 |
| SEC-04 供应链风险 | 🟢 Safe | 纯 Python 标准库 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入状态文件和配置文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 零 AI 设计，不涉及模型 |
| SEC-07 越权操作 | 🟢 Safe | 仅读取 ADS-B 数据并发送通知 |
| SEC-08 持久化机制 | 🟡 Medium | 设计为 cron 定期运行，含文件锁 |
| SEC-09 信息采集 | 🟡 Medium | 采集本地 ADS-B 航空数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码结构清晰 |

**综合评级: 🟢 Low**
**风险摘要:** 设计良好的零 AI 通知工具，功能单一透明

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
