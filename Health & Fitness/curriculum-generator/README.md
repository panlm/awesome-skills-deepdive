# Curriculum Generator

> Intelligent educational curriculum generation system with strict step enforcement and human escalation policies

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Curriculum Generator |
| **作者** | tarasinghrajput |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/tarasinghrajput-curriculum-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tarasinghrajput/curriculum-generator |
| **安全评级** | 🔴 High |

## 功能概述
- ✅ Guided requirement gathering through structured questionnaires
- ✅ Research-based curriculum design and assessment
- ✅ Automatic resource link population via web search
- ✅ Excel/CSV output generation
- ✅ Local memory storage for continuous improvement
- ✅ Strict step enforcement with human escalation policies
- ✅ Background task execution support
- Target audience (age, grade, background)

## 使用场景
- 健康数据管理与分析
- 健身目标跟踪
- 个人健康报告生成

## 依赖和前提条件
- Node.js / npm
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；文件系统篡改：涉及危险文件操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23