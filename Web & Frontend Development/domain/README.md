# DomainKits

> 全方位域名数据与洞察工具：可用性查询、WHOIS/DNS 记录、市场估值、趋势分析、品牌冲突检测，让 AI 成为你的域名投资助手。

## 功能概述

- **域名搜索与发现**：新注册域名、过期域名、已删除域名、老域名（5-20+ 年历史）、活跃站点等多维度搜索
- **可用性与定价**：单域名或批量查询可用性，支持跨 TLD 检查，实时显示注册价格
- **WHOIS / DNS / 安全检查**：一站式获取注册信息、DNS 记录和 Google Safe Browsing 安全状态
- **市场估值与 SEO 分析**：二级市场价格估算、反向链接分析、关键词数据（需账号）
- **趋势与情报**：注册热词趋势、TLD 增长排名、域名市场快报
- **智能工作流**：综合审计（analyze）、品牌冲突检测（brand_match）、替代域名推荐（plan_b）、创意域名生成器、过期域名尽职调查、比较市场估值（CMA）
- **个人工具**：偏好记忆、域名监控（自动 WHOIS/DNS 变化检测）、自动化机会发现策略

## 使用场景

- **品牌建站**：为新产品构思域名，批量验证可用性并比较价格，一步到位完成注册
- **域名投资**：追踪过期/删除域名，分析反向链接价值，发现趋势关键词抢注机会
- **品牌保护**：跨 TLD 检查品牌名占用情况，监控目标域名的注册和 NS 变更

## 依赖和前提条件

- **API 密钥**：`DOMAINKITS_API_KEY`（可选，免费账号即可获取更高配额和记忆功能）
- **MCP 客户端**：支持 Claude Code、Cursor 等主流 MCP 客户端
- **服务端点**：`https://api.domainkits.com/v1/mcp`

### 访问等级

| 等级 | 说明 |
|---|---|
| Guest（无需注册） | 大部分工具可用，每日限额较低 |
| Member（免费注册） | 全部工具，更高限额，记忆功能 |
| AI Access | 更高每日限额，更多监控和策略 |
| Premium | 完全访问，最高限额 |
| Platinum | 无限制 |

## 安全状态

| 检查项 | 状态 |
|---|---|
| VirusTotal | Benign |
| OpenClaw | Unknown |
| 综合评级 | ⚪ 部分未知 |

> OC 状态为 Unknown，但 VirusTotal 报告 Benign。该 Skill 通过 MCP 远程 API 调用工作，不包含本地脚本或可执行代码，风险较低。

## 包含文件

| 文件 | 说明 |
|---|---|
| `skill.md` | Skill 定义文件（工具列表、配置说明、使用指南） |
| `_meta.json` | 元数据（版本 v2.0.4，含 6 个历史版本） |

## 版本变更（v2.0.4）

- 大幅扩展工具集：新增 `domain_changes`、`price`、`market_price`、`keyword_intel`、`market_beat`、`name_advisor`、`valuation_cma` 等工作流工具
- 新增"个人工具"类别：偏好管理、域名监控、策略自动化、用量查询
- 工具分类重组，描述更准确
- 新增 AI Access 访问等级
- 从 v1.0.x 升级到 v2.0.x 系列

## 相关链接

- 官网：https://domainkits.com/mcp
- GitHub：https://github.com/ABTdomain/domainkits-mcp
- ClawHub：https://clawskills.sh/skills/abtdomain-domain

---
*由 awesome-skills-deepdive 自动生成 | 2026-03-28*
