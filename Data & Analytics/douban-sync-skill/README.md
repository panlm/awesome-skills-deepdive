# douban-sync-skill

> 导出和同步豆瓣（Douban）图书/电影/音乐/游戏收藏到本地 CSV

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | douban-sync-skill |
| **作者** | cosformula |
| **ClawHub** | https://clawskills.sh/skills/cosformula-douban-sync-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cosformula/douban-sync-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 全量导出豆瓣收藏（图书/电影/音乐/游戏）
- RSS 增量同步（无需登录）
- 浏览器自动化抓取（Puppeteer CDP）
- HTTP 直接抓取
- 输出 Obsidian 兼容 CSV 格式
- URL 去重和速率限制

## 使用场景
- 导出个人豆瓣收藏记录到本地
- 设置每日自动增量同步
- 与 Obsidian 等笔记工具集成

## 依赖和前提条件
- `DOUBAN_USER` 环境变量
- Node.js
- 可选：浏览器（用于 CDP 抓取）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| scripts/douban-scraper.mjs | HTTP 抓取器 |
| scripts/douban-browser-scraper.mjs | 浏览器 CDP 抓取器 |
| scripts/douban-extract.mjs | 浏览器控制台提取脚本 |
| scripts/douban-rss-sync.mjs | RSS 增量同步 |
| scripts/lib.mjs | 共享工具函数 |
| scripts/migrate-md-to-csv.mjs | MD 转 CSV 迁移工具 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Node.js 脚本，无 shell 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅与豆瓣网站通信 |
| SEC-03 凭证获取 | 🟡 Medium | 浏览器模式可能使用登录 Cookie |
| SEC-04 供应链风险 | 🟢 Safe | 无外部 npm 依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 CSV 文件和状态文件到 ~/douban-sync |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 仅访问用户自己的公开收藏 |
| SEC-08 持久化机制 | 🟡 Medium | 状态文件 .douban-rss-state.json 用于增量同步 |
| SEC-09 信息采集 | 🟡 Medium | 抓取豆瓣个人收藏数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读，有良好的输入验证 |

**综合评级: 🟡 Medium**
**风险摘要:** 豆瓣数据抓取工具，涉及用户数据和浏览器 Cookie 使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
