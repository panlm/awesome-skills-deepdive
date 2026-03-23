# Roster

> 从 CSV 可用性数据创建每周排班表并推送到 GitHub，专为外勤销售团队优化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Roster |
| **作者** | kleberbaum |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/kleberbaum-roster |

## 功能概述
- 处理 Google Forms CSV 文件，导入可用性、车辆信息和备注数据
- 自动从 CSV 日期列检测日历周（ISO 8601 标准）
- 智能排班：考虑出发时间、结束时间、车辆载客量（5人）、培训师分配等因素
- 自动检测 CSV 中的未知员工姓名并添加到员工列表
- 强制验证：时间窗口、培训师优先级、容量、工时限制
- 通过 Telegram 发送格式化的排班预览
- 确认后将 JSON 推送到 GitHub，触发 GitHub Actions 生成 PDF 和邮件发送
- 未成年人保护规则和每周工时限制管理

## 使用场景
- 外勤销售团队每周从 Google Forms 收集可用性数据后，自动生成排班计划
- 需要管理司机分配、培训师指派和车辆容量约束的团队排班
- 通过 Telegram 预览确认后自动推送排班并触发 PDF 生成和邮件分发

## 依赖和前提条件
- OpenClaw >= 0.8.0
- GitHub 仓库包含 `employees.json` 和 GitHub Actions 工作流（`build-roster.yml`、`publish-roster.yml`）
- 环境变量 `GITHUB_TOKEN`：具有 `repo` + `actions:write` 权限的 GitHub PAT
- 环境变量 `ROSTER_REPO`：GitHub 仓库名（`owner/repo` 格式）
- Python 3、`curl`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
