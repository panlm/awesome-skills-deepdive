# Finance News Briefings

> 带 AI 智能摘要的金融市场新闻简报工具，快速获取股票和市场动态资讯

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Finance News Briefings |
| **作者** | kesslerio |
| **版本** | 1.0.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-finance-news |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/finance-news |
| **安全评级** | 🔴 High |

## 功能概述
- 聚合多来源的金融新闻
- AI 生成新闻摘要和要点
- 按股票代码或行业筛选新闻
- 市场动态实时追踪
- 新闻情绪分析和影响评估
- 定时推送新闻简报

## 使用场景
- 投资者快速了解市场最新动态
- 追踪特定股票或行业的相关新闻
- 每日市场新闻简报自动生成

## 依赖和前提条件
- OpenClaw 环境已配置
- 金融新闻 API 密钥（如需要）

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `config`
- `docs`
- `htmlcov`
- `pyproject.toml`
- `pytest.ini`
- `requirements-test.txt`
- `requirements.txt`
- `scripts`
- `tests`
- `workflows`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，5 项中风险。持久化机制：设置系统级持久化；信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
