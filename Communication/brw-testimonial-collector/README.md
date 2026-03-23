# Testimonial Collector

> 系统化收集和格式化客户推荐评价的工具，帮助企业高效管理社会证明素材

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Testimonial Collector |
| **作者** | brianrwagner |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/brianrwagner-brw-testimonial-collector |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianrwagner/brw-testimonial-collector |
| **安全评级** | 🟢 Low |

## 功能概述
- 结构化收集客户推荐和评价内容
- 自动格式化评价为标准展示模板
- 分类管理不同类型的客户反馈
- 生成可用于营销的推荐语素材
- 支持多种输出格式（网页、社交媒体、PDF）

## 使用场景
- 企业系统化收集和整理客户好评用于官网展示
- 营销团队快速获取格式统一的客户推荐素材
- 产品团队收集用户反馈用于改进和宣传

## 依赖和前提条件
- 配置评价收集渠道和模板
- 已有客户联系信息或反馈来源

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
