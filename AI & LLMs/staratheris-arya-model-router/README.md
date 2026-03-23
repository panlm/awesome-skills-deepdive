# Arya Model Router

> Token-saver router: elige modelo (cheap/default/pro) y usa sub-agentes para tareas pesadas. Incluye compresión/briefing opcional.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arya Model Router |
| **作者** | staratheris |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/staratheris-staratheris-arya-model-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/staratheris/staratheris-arya-model-router |
| **安全评级** | 🟡 Medium |

## 功能概述
- Routes each request to one of: `cheap`, `default`, `pro`, `ultra`
- Supports manual overrides (`@cheap`, `@default`, `@pro`, `@ultra`)
- Supports router mode commands:
- `router status`
- `router auto on`
- `router auto off`
- Adds a feedback loop:
- `router feedback expensive` (or `router feedback caro`)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `brief.py`
- `router.py`
- `rules.json`
- `state.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23