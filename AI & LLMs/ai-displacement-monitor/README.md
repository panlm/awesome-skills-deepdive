# AI Displacement Monitor

> 监控 AI 驱动的白领劳动力替代早期预警信号及宏观金融溢出效应

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AI Displacement Monitor |
| **作者** | spyfree |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/spyfree-ai-displacement-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/spyfree/ai-displacement-monitor |
| **安全评级** | 🟢 Low |

## 功能概述
- 追踪 10 个关键指标组成的信号面板，包含最新值、方向和阈值状态
- 三层指标体系：领先劳动需求（A 层）、劳动市场确认（B 层）、消费/信贷溢出（C 层）
- 根据触发指标数量自动生成综合风险灯（绿/黄/橙/红）
- 提供可操作的投资组合和风险姿态建议
- 运用"工业革命透镜"对比替代速度与再吸收速度
- 识别数据缺口和过时输入

## 使用场景
- 为投资决策提供 AI 劳动力替代风险的量化参考
- 定期生成 AI 对就业市场影响的结构化风险报告
- 监控消费和信贷领域的 AI 溢出效应预警

## 依赖和前提条件
- 阈值配置文件（references/thresholds.example.json）
- 外部经济数据源（就业、消费、信贷指标）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
