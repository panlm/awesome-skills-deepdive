# AI Brand Analyzer

> 使用 AI 分析品牌并生成结构化品牌身份档案（JSON 格式）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AI Brand Analyzer |
| **作者** | pauldelavallaz |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/pauldelavallaz-ai-brand-analyzer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ai-brand-analyzer |
| **安全评级** | 🟡 Medium |

## 功能概述
- 通过 Google 搜索研究品牌的官方数据、营销活动和视觉形象
- 使用 Gemini Flash 配合搜索落地功能进行品牌分析
- 生成标准化 JSON 格式的品牌身份档案
- 分析品牌行为模式、视觉风格、摄影风格和语调
- 支持将档案存储并在 Ad-Ready 等创意工作流中复用
- 可列出已有品牌档案并进行更新

## 使用场景
- 为广告创意生成前快速建立品牌身份档案
- 分析竞争品牌的视觉风格和市场定位
- 在多个创意工具间共享标准化品牌数据

## 依赖和前提条件
- Gemini API Key（`GEMINI_API_KEY` 环境变量）
- uv 包管理器（用于运行 Python 脚本）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
