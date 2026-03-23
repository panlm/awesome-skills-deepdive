# context-compression

> 上下文压缩技能，优化长对话的 token 使用量和上下文窗口管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | context-compression |
| **作者** | leoyessi10-tech |
| **ClawHub** | https://clawskills.sh/skills/leoyessi10-tech-context-engineering |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leoyessi10-tech/context-engineering |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Agent sessions exceed context window limits
- Codebases exceed context windows (5M+ token systems)
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality
- Which files were created

## 依赖和前提条件
- Planning Phase**: Convert research into implementation specification with function signatures, type definitions, and data flow. A 5M token codebase compresses to approximately 2,000 words of specification.
- Implementation Phase**: Execute against the specification. Context remains focused on the spec rather than raw codebase exploration.

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
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