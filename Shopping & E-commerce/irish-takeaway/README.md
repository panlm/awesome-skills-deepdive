# irish-takeaway

> 爱尔兰外卖订餐助手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | irish-takeaway |
| **作者** | cotyledonlab |
| **ClawHub** | https://clawskills.sh/skills/cotyledonlab-irish-takeaway |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cotyledonlab/irish-takeaway |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🔍 Find nearby takeaways using Google Places API
- 📋 Browse menus via Deliveroo/Just Eat browser automation
- 🇮🇪 Irish-focused with pre-configured town coordinates
- ⭐ Filter by rating, cuisine type, and open status
- Drogheda, Dublin, Cork, Galway, Limerick
- Waterford, Dundalk, Swords, Navan, Bray

## 依赖和前提条件
- Set API key: `export GOOGLE_PLACES_API_KEY="your-key"`

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `search-takeaways.sh` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
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