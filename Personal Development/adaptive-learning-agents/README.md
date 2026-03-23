# adaptive-learning-agents

> 自适应学习 Agent — 从错误和反馈中实时学习改进

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | adaptive-learning-agents |
| **作者** | vedantsingh60 |
| **ClawHub** | https://clawskills.sh/skills/vedantsingh60-adaptive-learning-agents |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vedantsingh60/adaptive-learning-agents |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Learn from errors and corrections in real-time. Continuously improve by capturing failures, user feedback, and successful patterns.
- Mistakes that need correction
- Unexpected API behaviors
- Better approaches discovered through experimentation
- Knowledge gaps that get revealed during use
- Adaptive Learning Agent captures every error, correction, and successful pattern automatically. Then retrieves relevant learnings before tackling similar problems again.

## 依赖和前提条件
- 
- 
- MIT Licensed** - Free to use, modify, redistribute
- Comprehensive API** - Simple, Pythonic interface
- 

## 包含文件
- `LICENSE.md`
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `adaptive_learning_agent.py` — 脚本文件
- `manifest.yaml` — 配置/数据文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
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