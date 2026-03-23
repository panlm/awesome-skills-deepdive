# Blog Writer

> This skill should be used when writing blog posts, articles, or long-form content in the writer's distinctive writing style. It produces authentic, opinionated content that matches the writer's voice—direct, conversational, and grounded in personal experience. The skill handles the complete workflow from research review through Notion publication. Use this skill for drafting blog posts, thought leadership pieces, or any writing meant to reflect the writer's perspective on AI, productivity, sales, marketing, or technology topics.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Blog Writer |
| **作者** | tomstools11 |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/tomstools11-blog-writer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tomstools11/blog-writer |
| **安全评级** | 🟡 Medium |

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 包含文件
- `2024-02-17-radical-transparency-sales.md`
- `2024-02-17-raycast-spotlight-superpowers.md`
- `2024-02-17-short-form-content-marketing.md`
- `2024-02-17-typing-speed-benefits.md`
- `2024-03-14-effective-ai-prompts.md`
- `2024-11-08-ai-revolutionizing-entry-level-sales.md`
- `2025-11-12-why-ai-art-is-useless.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `manage_examples.py`
- `style-guide.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23