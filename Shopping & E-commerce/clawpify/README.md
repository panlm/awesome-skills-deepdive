# clawpify

> Spotify 风格的音乐推荐和播放管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawpify |
| **作者** | alhwyn |
| **ClawHub** | https://clawskills.sh/skills/alhwyn-clawpify |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alhwyn/clawpify |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Tool: shopify_graphql (from MCP server or custom function)
- Products (list, search, create, update, delete)
- Orders (view, cancel, fulfill)
- Customers (list, create, update)
- Inventory (check levels, adjust quantities)
- Discounts (create codes, manage promotions)

## 依赖和前提条件
- Tool: shopify_graphql (from MCP server or custom function)
- 
- menus.md - Navigation menus
- metafields.md - Custom data fields
- pages.md - Store pages

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 存在网络通信 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23