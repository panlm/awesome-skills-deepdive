# Gumroad Analytics

> 从 Gumroad API 拉取产品和销售数据，用于追踪分析和营销效果评估。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Gumroad Analytics |
| **作者** | vladchatware |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/vladchatware-gumroad-analytics |

## 功能概述
- 快速查看所有产品及热门产品统计
- 每日自动记录指标快照，用于趋势分析
- 按日期或产品过滤导出销售数据
- 无需 jq 依赖，仅使用基本 Shell 工具
- 支持与营销活动进行关联分析

## 使用场景
- 追踪 Gumroad 数字产品的销售趋势和收入变化
- 将销售数据与营销活动关联，评估推广效果
- 每日自动生成产品表现报告

## 依赖和前提条件
- Gumroad API Token（从 Gumroad → Settings → Advanced → Applications 获取）
- 环境变量：`GUMROAD_ACCESS_TOKEN`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
