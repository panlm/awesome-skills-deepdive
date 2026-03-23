# Meta Tags Optimizer

> 'This skill should be used when the user asks to "optimize title tag", "write meta description", "improve CTR", "Open Graph tags", "social media preview", "my title tag needs work", "low click-through rate", "fix my meta tags", or "OG tags not showing". Creates and optimizes meta tags including title tags, meta descriptions, Open Graph tags, and Twitter cards for maximum click-through rates and social sharing engagement. For a broader on-page audit, see on-page-seo-auditor. For structured data markup, see schema-markup-generator.'

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Meta Tags Optimizer |
| **作者** | aaron-he-zhu |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/aaron-he-zhu-meta-tags-optimizer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aaron-he-zhu/meta-tags-optimizer |
| **安全评级** | 🟢 Low |

## 功能概述
- meta-description
- social-sharing
- "optimize title tag"
- "write meta description"
- "Open Graph tags"
- "social media preview"

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23