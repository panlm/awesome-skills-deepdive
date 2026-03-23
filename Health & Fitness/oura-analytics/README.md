# Oura Ring Analytics

> Oura Ring data integration and analytics. Fetch sleep scores, readiness, activity, HRV, and trends from the Oura Cloud API. Generate automated reports, correlations with productivity, and trigger-based alerts for low recovery days. Requires OURA_API_TOKEN (get at cloud.ouraring.com).

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Oura Ring Analytics |
| **作者** | kesslerio |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-oura-analytics |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/oura-analytics |
| **安全评级** | 🔴 High |

## 功能概述
- Daily morning briefings ("How did I sleep?")
- Correlating recovery with productivity/calendar
- Automated alerts for low recovery days
- Weekly/monthly health trend reports
- Simple Python API client for Oura Cloud API v2
- Trend analysis and correlation tools

## 使用场景
- 同步和分析运动数据
- 追踪健康指标趋势
- 生成健身报告和洞察

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SECURITY.md`
- `SKILL.md`
- `_meta.json`
- `pyproject.toml`
- `references`
- `requirements-dev.txt`
- `requirements.txt`
- `scripts`
- `tests`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23