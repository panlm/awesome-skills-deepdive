# insta-cog

> Instagram 内容分析和管理认知工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | insta-cog |
| **作者** | nitishgargiitd |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/nitishgargiitd-insta-cog |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/insta-cog |
| **安全评级** | 🟢 Low |

## 功能概述
- Trending Format Videos: "Create a 15-second Reel using the 'day in my life' format for a coffee shop"
- Product Showcases: "Make a TikTok showing our new sneakers with trending transitions"
- Educational Clips: "Create a 30-second explainer about compound interest for Gen Z"
- Behind-the-Scenes: "Make a BTS Reel of a bakery kitchen with satisfying visuals"
- Transformation Videos: "Create a before/after transformation Reel for a home renovation"
- Educational Carousels: "Create a 10-slide carousel explaining how to start investing"
- Listicles: "Make a '7 productivity hacks' carousel with bold graphics"
- Storytelling: "Create a carousel telling our brand's origin story"

## 使用场景
- 分析 Instagram 账号的内容表现
- 管理帖子发布计划
- 获取 Instagram 互动数据

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
