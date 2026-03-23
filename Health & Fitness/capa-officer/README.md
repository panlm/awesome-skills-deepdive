# Capa Officer

> CAPA（纠正和预防措施）管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Capa Officer |
| **作者** | alirezarezvani |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-capa-officer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/capa-officer |
| **安全评级** | 🟢 Low |

## 功能概述
- CAPA Investigation Workflow
- Root Cause Analysis
- Corrective Action Planning
- Effectiveness Verification
- CAPA Metrics and Reporting
- Reference Documentation
- Tools
- [ ] Problem description with specific details (what, where, when, who, how much)

## 使用场景
- 记录和跟踪质量问题的纠正措施
- 管理预防措施的实施进度
- 生成 CAPA 合规性报告

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
