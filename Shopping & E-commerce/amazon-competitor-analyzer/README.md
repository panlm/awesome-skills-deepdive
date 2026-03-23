# amazon-competitor-analyzer

> 使用浏览器自动化抓取 Amazon 商品数据，进行竞品深度分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | amazon-competitor-analyzer |
| **作者** | phheng |
| **ClawHub** | https://clawskills.sh/skills/phheng-amazon-competitor-analyzer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/phheng/amazon-competitor-analyzer |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- BROWSERACT_API_KEY
- Competitive research: Input multiple ASINs to understand market landscape
- Pricing strategy analysis: Compare price bands across similar products
- Specification benchmarking: Deep dive into technical specs and feature differences
- Review insights: Analyze review quality, quantity, and sentiment patterns
- Market opportunity discovery: Identify gaps and potential threats

## 依赖和前提条件
- Visit [browseract.com](https://browseract.com)
- Sign up for an account
- Navigate to [API Settings](https://www.browseract.com/reception/integrations)

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `amazon_competitor_analyzer.py` — 脚本文件

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