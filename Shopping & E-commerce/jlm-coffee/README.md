# jlm-coffee

> 咖啡豆推荐和咖啡知识查询

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | jlm-coffee |
| **作者** | alexpolonsky |
| **ClawHub** | https://clawskills.sh/skills/alexpolonsky-jlm-coffee |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alexpolonsky/jlm-coffee |
| **许可证** | MIT |
| **安全评级** | 🟡 Medium |

## 功能概述
- Community-curated: All specialty coffee in Jerusalem, community-reviewed
- Official data source: Reads from a public JSON export provided by the site maintainer (no API key, no Firestore)
- Bilingual: Search works with Hebrew and English names
- Opening hours: Based on Google Places data, cached by the site
- Reviews included: Shop details show community reviews with ratings
- Color output: ANSI colors in terminal (respects `NO_COLOR` env var and `--no-color` flag)

## 依赖和前提条件
- Fast caching**: 15-minute local cache TTL - one fetch covers all commands

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