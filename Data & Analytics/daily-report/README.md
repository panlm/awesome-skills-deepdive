# daily-report

> 追踪销售线索进度、生成指标报告和管理记忆文件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | daily-report |
| **作者** | visualdeptcreative |
| **ClawHub** | https://clawskills.sh/skills/visualdeptcreative-daily-report |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/daily-report |
| **安全评级** | 🟢 Low |

## 功能概述
- 生成每日晨间简报（Pipeline 状态、过夜数据、预算）
- 生成每日结束报告（当日数字、成本、热点线索）
- 每周总结报告（线索/外展/回复/成交汇总）
- 追踪预算使用情况
- 管理本地记忆文件

## 使用场景
- 销售团队每日运营报告自动化
- 线索开发和外展活动追踪
- 预算和成本监控

## 依赖和前提条件
- 本地 Ollama 模型（免费）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含报告模板 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，无脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地操作 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅写入 memory 目录 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 记忆文件属预期功能 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯报告模板，无脚本执行，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
