# FLWR Branding Studio Kit

> An advanced AI agent that acts as a Senior Brand Strategist. It automates project setup, applies elite market methodologies (Archetypes, StoryBrand, Personas), and generates structured brand assets while preventing hallucinations via strict context shielding.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | FLWR Branding Studio Kit |
| **作者** | vansearch |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/vansearch-flwr-branding-studio-kit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vansearch/flwr-branding-studio-kit |
| **安全评级** | 🟡 Medium |

## 功能概述
- RACE Framework Integration: Deep integration of the Research, Action, Context, Example methodology.
- Context Shielding Protocol: Prevents cross-contamination between clients. The structure is fixed; the content is fluid.
- Anti-Slop Writing Checks: Automated rules to prevent generic AI copywriting (no "delve", "tapestry", or sequential adjec
- 🎨 Asset Output: Generates assets in a specific Markdown format.
- Automated Project Setup: One-command initialization for new client projects.
- `.agent/rules/`: The "brain" of the strategist (`branding_agent_rules.md`).

## 使用场景
- 品牌形象管理和维护
- 品牌声音一致性
- 品牌资产管理

## 依赖和前提条件
- Node.js / npm
- Python / pip
- macOS

## 包含文件
- `CONTRIBUTING.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `bin`
- `docs`
- `package.json`
- `requirements.txt`
- `task.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23