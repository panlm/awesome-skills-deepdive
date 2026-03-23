# clawver-store-analytics

> 监控 Clawver 商店绩效，查询收入、热销产品和转化率

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawver-store-analytics |
| **作者** | nwang783 |
| **ClawHub** | https://clawskills.sh/skills/nwang783-clawver-store-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-store-analytics |
| **安全评级** | 🟢 Low |

## 功能概述
- 获取商店总收入、订单数、平均订单金额等汇总数据
- 查看热销产品排名及转化率
- 按时间段筛选分析（7天/30天/90天）
- 查看产品评分和评论数据
- 管理产品和商店设置
- 支持 Stripe 支付集成

## 使用场景
- 日常商店运营数据监控
- 产品销售表现分析
- 收入增长趋势追踪

## 依赖和前提条件
- `CLAW_API_KEY` 环境变量
- 已激活的 Clawver 商店

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含 API 使用方法 |
| references/api-examples.md | API 调用示例参考 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 curl 调用 API，无危险命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 Clawver 官方 API 通信 |
| SEC-03 凭证获取 | 🟢 Safe | 从环境变量读取 API Key |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 Clawver 官方 API |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 API 授权范围内操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取用户自己的商店数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的只读 API 客户端，仅获取商店分析数据

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
