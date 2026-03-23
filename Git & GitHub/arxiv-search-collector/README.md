# Arxiv Search Collector

> 模型驱动的 arXiv 论文检索工作流，由 AI 规划查询策略并筛选相关论文，构建高质量论文集

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arxiv Search Collector |
| **作者** | xukp20 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/xukp20-arxiv-search-collector |

## 功能概述
- 初始化检索任务，设置主题、关键词、分类、目标论文数量和回溯天数
- 模型自主设计多个检索查询（支持 OR/AND 语法），按语义分组扩展覆盖面
- 批量执行查询（内置速率限制、指数退避重试、最大 60 条/查询）
- 模型逐查询审阅结果，通过 keep index 筛选相关论文
- 自动合并和去重所有保留的论文，生成统一的论文集
- 支持多语言输出（如中文），元数据和摘要以指定语言生成
- 为每篇论文创建独立元数据目录和汇总索引

## 使用场景
- 针对特定研究方向系统性收集最新 arXiv 论文
- 利用 AI 的语义理解能力设计查询策略，避免遗漏相关工作
- 构建研究综述所需的论文基础数据集

## 依赖和前提条件
- `python3`
- 需要网络访问 arXiv API
- 脚本位于 `scripts/` 目录（init_collection_run.py、fetch_queries_batch.py 等）

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
