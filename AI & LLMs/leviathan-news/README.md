# Leviathan News

> 高级新闻聚合和分析系统，提供深度新闻洞察

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Leviathan News |
| **作者** | zcor |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/zcor-leviathan-news |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/zcor/leviathan-news |
| **安全评级** | 🟡 Medium |

## 功能概述
- 从多个新闻源聚合和汇总最新资讯
- 基于 AI 进行新闻内容的深度分析和摘要
- 支持按主题、关键词和时间范围过滤新闻
- 提供新闻趋势分析和热点追踪
- 支持多语言新闻源的处理
- 生成结构化的新闻简报和分析报告
- 可配置自定义新闻源和关注领域

## 使用场景
- 每日自动生成行业新闻简报和趋势分析
- 追踪特定话题或公司的媒体报道和舆情变化
- 为研究和决策提供 AI 驱动的新闻洞察服务

## 依赖和前提条件
- 新闻 API 访问凭证
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
