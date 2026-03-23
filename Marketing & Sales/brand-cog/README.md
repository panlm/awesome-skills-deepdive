# brand-cog

> "Other tools make logos. CellCog builds brands. #1 on DeepResearch Bench (Feb 2026) for deep strategic reasoning + the widest modality coverage in AI. Brand identity, brand kits, color palettes, typography, brand guidelines, logo design, visual identity, social media, web design, video — all from one brief."

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | brand-cog |
| **作者** | nitishgargiitd |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/nitishgargiitd-brand-cog |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/brand-cog |
| **安全评级** | 🟡 Medium |

## 功能概述
- Visual Consistency: Every touchpoint must feel cohesive
- Strategic Positioning: Design reflects brand personality and values
- Versatility: Works across social media, print, web, merchandise
- Memorability: Distinctive enough to stick in minds
- Scalability: From favicon to billboard
- Startup Brand Kits: "Create a complete brand identity for my SaaS startup"

## 使用场景
- 品牌形象管理和维护
- 品牌声音一致性
- 品牌资产管理

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

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
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。持久化机制：设置系统级持久化

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23