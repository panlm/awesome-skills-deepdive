# Ai Trend Curation

> 从 X（Twitter）收集 AI 趋势推文并生成引用建议，发布到 Slack

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai Trend Curation |
| **作者** | yusaku-0426 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/yusaku-0426-ai-trend-curation |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yusaku-0426/ai-trend-curation |
| **安全评级** | 🟢 Low |

## 功能概述
- 使用 xurl CLI 搜索日文和英文的 AI 相关热门推文
- 按互动量筛选（日文 100+ 赞、英文 500+ 赞）
- 智能选取 5-8 条推文，排除标题党和炒作内容
- 为每条推文生成分类、作者描述和引用建议
- 将策展结果格式化为 Slack Block Kit 并发布
- 支持重复检查和已发布标记追踪
- 提供 8 种引用模式：要点抜粋、注目点指摘、活用报告等

## 使用场景
- 每日自动策展 AI 领域的高质量推文并推送到 Slack 频道
- 为个人品牌运营生成有洞察力的引用推文建议

## 依赖和前提条件
- xurl CLI 工具
- Node.js（运行 scripts/ai_trends.js）
- OpenClaw message 工具（发送 Slack 消息）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
