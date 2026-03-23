# lg-thinq

> 通过 LG ThinQ API 控制 LG 智能家电（洗衣机/空调/冰箱等）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | lg-thinq |
| **作者** | kaiofreitas |
| **ClawHub** | https://clawskills.sh/skills/kaiofreitas-lg-thinq |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kaiofreitas/lg-thinq |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Fridge: 0°C to 6°C
- Freezer: -24°C to -14°C (varies by model)
- "check my fridge" → `status fridge`
- "set fridge to 5 degrees" → `fridge-temp 5`
- "turn on express freeze" → `express-freeze on`
- "is the fridge door open?" → `status fridge` (check doorStatus)

## 依赖和前提条件
- Get a Personal Access Token from https://connect-pat.lgthinq.com
- Store token: `echo "YOUR_TOKEN" > ~/.config/lg-thinq/token`
- Store country code: `echo "MX" > ~/.config/lg-thinq/country`

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