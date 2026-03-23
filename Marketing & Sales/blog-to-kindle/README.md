# Blog to Kindle

> Scrape blogs/essay sites and compile into Kindle-friendly EPUB with AI-generated cover. Use for requests to download blogs for Kindle, compile essays into ebook, or send blog archives to Kindle. Supports Paul Graham, Kevin Kelly, Derek Sivers, Wait But Why, Astral Codex Ten, and custom sites.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Blog to Kindle |
| **作者** | ainekomacx |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/ainekomacx-blog-to-kindle |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ainekomacx/blog-to-kindle |
| **安全评级** | 🟡 Medium |

## 功能概述
- Sender email is on Kindle approved list
- File under 50MB (EPUB compresses well)
- `{site}-last-fetch.json` - Last fetch timestamp, article count
- `{site}-sent.json` - List of sent article IDs

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- macOS

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23