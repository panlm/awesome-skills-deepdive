# agent-evolver

> AI Agent 自我进化引擎 — 从经验中学习、检测问题并优化策略

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-evolver |
| **作者** | lilei0311 |
| **ClawHub** | https://clawskills.sh/skills/lilei0311-agent-evolver |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lilei0311/agent-evolver |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- 当用户要求改进 Agent 性能时
- 使用 LLM 自动分析错误原因
- 使用 Embedding 模型向量化经验
- 代码生成 (code_generation)
- 数据分析 (data_analysis)
- 文档处理 (document_processing)

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `config/` — 目录
- `deploy.sh` — 脚本文件
- `evolver.sh` — 脚本文件
- `requirements.txt` — 配置/数据文件
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23