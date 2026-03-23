# Diet Tracker

> 饮食记录和营养分析跟踪工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Diet Tracker |
| **作者** | yonghaozhao722 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/yonghaozhao722-diet-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yonghaozhao722/diet-tracker |
| **安全评级** | 🟡 Medium |

## 功能概述
- "I had [food] for lunch/dinner"
- "What's my remaining calorie budget?"
- "How many calories have I eaten today?"
- "Log my meal"
- "Check my diet progress"
- Lunch reminder: ~12:30 (checks if lunch logged, sends reminder if not)
- Dinner reminder: ~18:00 (checks if dinner logged, sends reminder if not)
- Daily calorie target (default: 1650 kcal)

## 使用场景
- 记录每日三餐的饮食内容
- 计算营养成分和热量摄入
- 跟踪减重目标的达成进度

## 依赖和前提条件
- Python 3.x
- 数据库

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
