# Weekly Content Planner

> 每周内容规划和排期工具

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
- 7 days of posts (Mon–Sun)
- 3 platform variants per day (Twitter, LinkedIn, Instagram)
- Hashtag suggestions per platform
- Best posting times
- Content mix (educational, engagement, promotional, storytelling)
- Twitter/X: ≤280 chars, punchy, 2-3 hashtags, thread hooks
- LinkedIn: Professional tone, 1-3 paragraphs, thought leadership, 3-5 hashtags
- Instagram: Visual-first caption, storytelling, 5-10 hashtags, CTA in bio link

## 使用场景
- 制定每周内容创作计划
- 安排内容发布时间和平台
- 跟踪内容创作进度

## 依赖和前提条件
- pip / uv 包管理器
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`
- `example-output.md`
- `generate.sh`

## 安全状态
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
