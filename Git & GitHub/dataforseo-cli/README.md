# dataforseo-cli

> 面向 AI Agent 的 SEO 关键词研究 CLI 工具，通过 DataForSEO API 查询搜索量、CPC、关键词难度和竞争度

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | dataforseo-cli |
| **作者** | alexgusevski |
| **版本** | 1.0.6 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/alexgusevski-dataforseo-cli |

## 功能概述
- 查询关键词搜索量、CPC、关键词难度（0-100）、竞争级别和 12 个月趋势
- 根据种子关键词发现相关关键词建议
- 分析竞争对手域名当前排名的关键词
- 默认输出 TSV 格式，针对 LLM 上下文窗口优化（最省 token）
- 支持 JSON 和人类可读表格等多种输出格式
- 离线查询地区代码和语言代码（无需 API 凭证）
- 支持批量关键词查询以节省 API 请求次数

## 使用场景
- 做内容规划时研究目标关键词的搜索量和竞争难度
- 分析竞品网站的关键词排名策略，找到流量缺口
- AI Agent 自动执行 SEO 研究任务，输出紧凑的 TSV 数据

## 依赖和前提条件
- Node.js（通过 npm 全局安装：`npm install -g dataforseo-cli`）
- DataForSEO API 凭证（login + password 或 base64 token）
- 凭证存储在 `~/.config/dataforseo-cli/config.json`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
