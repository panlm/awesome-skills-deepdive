# ceorater

> 获取标普 500 公司 CEO 绩效的机构级分析数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ceorater |
| **作者** | ceorater-skills |
| **ClawHub** | https://clawskills.sh/skills/ceorater-skills-ceorater |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ceorater-skills/ceorater |
| **安全评级** | 🟢 Low |

## 功能概述
- 查询 CEO 综合评分（CEORaterScore 0-100）
- 获取市场超额收益指标（AlphaScore）
- 分析收入复合增长率（RevenueCAGRScore）
- 评估薪酬效率等级（CompScore A-F）
- 支持按股票代码、CEO 姓名、行业搜索
- 覆盖 500+ 位美国上市公司 CEO

## 使用场景
- 比较不同公司 CEO 绩效
- 投资研究中的管理层分析
- 行业 CEO 排名查询

## 依赖和前提条件
- `CEORATER_API_KEY` 环境变量（需付费订阅 $99/月）
- curl, jq

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| ORIGINAL_README.md | 原始说明文档 |
| scripts/ceorater.sh | API 调用辅助脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 脚本有输入清理（sanitize），防注入处理良好 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与 CEORater 官方 API 通信 |
| SEC-03 凭证获取 | 🟢 Safe | 从环境变量读取 API Key，无硬编码 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 ceorater.com 官方 API |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 只读 API 调用 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化行为 |
| SEC-09 信息采集 | 🟢 Safe | 仅获取公开商业数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，有良好的输入验证 |

**综合评级: 🟢 Low**
**风险摘要:** 安全性良好的只读 API 客户端，有输入清理和验证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
