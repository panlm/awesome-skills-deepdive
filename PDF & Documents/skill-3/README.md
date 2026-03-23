# Skill 3

> Swiss-army knife for JSON files. Pretty-print, validate, minify, sort keys, and query with dot-notation paths. Zero dependencies.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill 3 |
| **作者** | claudiodrusus |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/claudiodrusus-skill-3 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/claudiodrusus/skill-3 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Pretty-print with configurable indentation (2, 4, or any number of spaces)
- Minify JSON to reduce file size for APIs and storage
- Validate JSON and get structural stats (type, key count, size)
- Query nested data with dot-notation paths including array indices
- Sort keys alphabetically for deterministic output and easier diffs
- Stdin support for use in shell pipelines with other tools

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `main.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。混淆/反分析：存在代码混淆或编码

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23