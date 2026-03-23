# yahoo-data-fetcher

> 从 Yahoo Finance 获取实时股票报价

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | yahoo-data-fetcher |
| **作者** | noypearl |
| **ClawHub** | https://clawskills.sh/skills/noypearl-yahoo-data-fetcher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/noypearl/yahoo-data-fetcher |
| **安全评级** | 🟢 Low |

## 功能概述
- 获取实时股票价格
- 支持多股票批量查询
- 返回价格、涨跌幅、市场状态等
- 支持 JSON/CLI 多种输入格式
- 未找到的股票返回 null 值
- 无需 API Key

## 使用场景
- 实时股票行情查询
- 投资组合监控
- 市场数据集成

## 依赖和前提条件
- Node.js

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| index.js | 股票查询核心脚本 |
| package.json | npm 配置 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 脚本，无 shell 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 Yahoo Finance API 通信 |
| SEC-03 凭证获取 | 🟢 Safe | 无需凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部 npm 依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 只读公开数据 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取公开股票数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 简洁安全的股票数据获取工具，无需认证，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
