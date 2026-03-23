# Amazon Product Api Skill

> 从亚马逊搜索结果中提取结构化商品数据，包括标题、ASIN、价格、评分和产品规格

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Amazon Product Api Skill |
| **作者** | phheng |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/phheng-amazon-product-api-skill |

## 功能概述
- 通过 BrowserAct API 从亚马逊搜索结果中提取产品列表
- 支持按关键词、品牌、页数和语言进行搜索配置
- 提取字段包括：商品标题、ASIN、当前/原始价格、平均评分、评分数量
- 自动绕过 reCAPTCHA 等反爬机制，无地理围栏限制
- 内置错误处理和自动重试机制（最多重试一次）
- 支持多语言和多市场搜索（如 zh-CN、de 等）
- 实时输出带时间戳的任务状态日志

## 使用场景
- 进行市场调研，分析特定品类的顶级品牌和定价策略
- 监控竞争对手的产品列表和价格变动
- 批量提取产品数据用于建立或更新产品数据库

## 依赖和前提条件
- 环境变量 `BROWSERACT_API_KEY`（从 [BrowserAct Console](https://www.browseract.com/reception/integrations) 获取）
- Python 运行环境
- 脚本文件 `scripts/amazon_product_api.py`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
