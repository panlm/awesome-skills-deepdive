# food-order

> AI 外卖点餐助手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | food-order |
| **作者** | steipete |
| **ClawHub** | https://clawskills.sh/skills/steipete-food-order |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/steipete/food-order |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Never run `ordercli foodora reorder ... --confirm` unless user explicitly confirms placing the order.
- Prefer preview-only steps first; show what will happen; ask for confirmation.
- If user is unsure: stop at preview and ask questions.
- Country: `ordercli foodora countries` → `ordercli foodora config set --country AT`
- Login (password): `ordercli foodora login --email you@example.com --password-stdin`
- Login (no password, preferred): `ordercli foodora session chrome --url https://www.foodora.at/ --profile "Default"`

## 依赖和前提条件
- 
- Country: `ordercli foodora countries` → `ordercli foodora config set --country AT`
- Login (password): `ordercli foodora login --email you@example.com --password-stdin`
- Login (no password, preferred): `ordercli foodora session chrome --url https://www.foodora.at/ --profile "Default"`
- Recent list: `ordercli foodora history --limit 10`

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件删除操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23