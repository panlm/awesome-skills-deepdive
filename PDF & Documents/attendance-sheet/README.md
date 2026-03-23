# Attendance Sheet

> 考勤表自动生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Attendance Sheet |
| **作者** | gykdly |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/gykdly-attendance-sheet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gykdly/attendance-sheet |
| **安全评级** | 🟢 Low |

## 功能概述
- 自动创建考勤记录表
- 支持多种考勤模板
- 数据统计和汇总功能
- 导出为标准表格格式

## 使用场景
- 为团队自动生成月度考勤统计表
- 创建活动签到和出勤记录表

## 依赖和前提条件
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23