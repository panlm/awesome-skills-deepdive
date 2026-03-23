# Copyku

> 印尼语 AI 文案专家，专注数字营销、社交媒体、落地页、广告和品牌定位的文案撰写。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Copyku |
| **作者** | khamalismadie |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/khamalismadie-copyku |

## 功能概述
- 三种工作模式：Quick Copy（快速生成）、Guided（逐步引导）、Advanced（完全控制）
- 支持 8 大平台输出：Instagram、TikTok、LinkedIn、Twitter/X、落地页、销售页、Email、广告
- 提供 23 种文案语调：说服、教育、叙事、高端、硬销、软销、幽默、权威等
- 内置 6 种经典文案公式：AIDA、PAS、BAB、4U、SSC、PASOC
- 支持 5 级用户认知水平适配：从完全无意识到已准备购买
- 完整的印尼语本地化，贴合当地市场和文化

## 使用场景
- 印尼市场的社交媒体营销文案批量生成（Instagram 配文 + 标签、TikTok 脚本等）
- 快速创建针对不同认知水平用户的落地页和销售页文案
- 为广告投放生成多版本的 Hook + Body + CTA 组合

## 依赖和前提条件
- 无外部依赖

## 安全状态
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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
