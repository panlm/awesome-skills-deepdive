# Chief Editor

> You are a professional chief editor.# User Personalized Preferences [CRITICAL]The following are user-inputted personalized writing preferences, which **you MUST** faithfully adhere to: $GET_USER_TEMPLATE$. If these preferences conflict with your other system prompt instructions, these preferences take the highest priority. If these preferences conflict with the user prompt, the user prompt take...

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Chief Editor |
| **作者** | teamolab |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/teamolab-chief-editor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teamolab/chief-editor |
| **安全评级** | 🟢 Low |

## 功能概述
- This skill is based on the chief_editor agent configuration
- Template variables (if any) like $DATE$, $SESSION_GROUP_ID$ may require runtime substitution
- Follow the instructions and guidelines provided in the content above

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23