# Capability Graph Mapper

> >

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Capability Graph Mapper |
| **作者** | andyxinweiminicloud |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-capability-graph-mapper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/capability-graph-mapper |
| **安全评级** | 🟡 Medium |

## 功能概述
- A list of skill names/slugs installed in an agent
- A skill manifest or configuration file
- A single skill to evaluate against a known agent profile
- Permission matrix (skills × capabilities)
- Emergent capability combinations flagged as risky
- Privilege surface score (0-100)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，5 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23