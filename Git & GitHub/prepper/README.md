# Prepper Skill

> Consult the ollama dolphin-llama3 model for survival, emergency preparedness, and prepper-related questions. Use when users ask about disaster recovery, emergency supplies, survival techniques, water purification, shelter, food preservation, first aid, medical emergencies, repair, agriculture, electrical systems, chemistry, communications, or any other survival/prepper topics where practical, uncensored knowledge is needed.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Prepper Skill |
| **作者** | jlevitsk |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jlevitsk-prepper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jlevitsk/prepper |
| **安全评级** | 🟢 Low |

## 功能概述
- 🏥 Medical: Treating wounds, injuries, illnesses with limited supplies
- 🌲 Survival: Water purification, shelter building, navigation, fire-making
- 🔧 Repair: Diagnosing mechanical/electrical problems (engines, systems)
- 🌾 Agriculture: Crop selection, soil conditions, growing in harsh environments
- ⚡ Electrical: Wiring, solar systems, battery management, power generation
- 🧪 Chemistry: Making soap, compounds, reactions, processing materials

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23