# Ad-Ready Pro

> Generate professional advertising images from product URLs using the Ad-Ready pipeline on ComfyDeploy. Use when the user wants to create ads for any product by providing a URL, optionally with a brand profile (70+ brands) and funnel stage targeting. Supports model/talent integration, brand-aware creative direction, and multi-format output. Differs from Morpheus (manual fashion photography) — Ad-Ready is URL-driven, brand-intelligent, and funnel-stage aware.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ad-Ready Pro |
| **作者** | pauldelavallaz |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/pauldelavallaz-ad-ready-pro |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready-pro |
| **安全评级** | 🟡 Medium |

## 功能概述
- Download the main product image from the product URL
- Search and download the brand logo
- Both get uploaded to ComfyDeploy automatically
- Gemini Flash visits the product URL
- Extracts: title, description, features, price, images
- ⚠️ Image scraping is the most fragile part — always provide product images manually

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
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