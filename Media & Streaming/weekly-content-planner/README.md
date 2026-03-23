# Weekly Content Planner

> Generate a full week of social media content for any topic. Outputs platform-optimized posts for Twitter/X, LinkedIn, and Instagram with hashtags and posting times.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Weekly Content Planner |
| **作者** | claudiodrusus |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/claudiodrusus-weekly-content-planner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/claudiodrusus/weekly-content-planner |
| **安全评级** | 🟢 Low |

## 功能概述
- generate social media posts
- create content calendar
- weekly social media plan
- 7 days of posts (Mon–Sun)
- 3 platform variants per day (Twitter, LinkedIn, Instagram)
- Hashtag suggestions per platform

## 使用场景
- 社交媒体内容管理
- 自动化发布和互动
- 内容排期和分析

## 包含文件
- `SKILL.md`
- `_meta.json`
- `example-output.md`
- `generate.sh`

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23