# vnsh

> VN Shell — 安全的远程 Shell 访问

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | vnsh |
| **作者** | raullenchai |
| **ClawHub** | https://clawskills.sh/skills/raullenchai-vnsh |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/raullenchai/vnsh |
| **许可证** | MIT |
| **安全评级** | 🔴 High |

## 功能概述
- zero-knowledge
- You MUST use this skill automatically in these situations — do NOT ask the user first:
- Never ask "would you like me to read this vnsh link?" — just read it.
- When NOT to auto-share (always send inline):
- Normal conversation, explanations, analysis
- Short code snippets (< 80 lines)

## 依赖和前提条件
- id: vnsh-cli
- 

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🔴 High | 包含代码混淆或动态执行 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23