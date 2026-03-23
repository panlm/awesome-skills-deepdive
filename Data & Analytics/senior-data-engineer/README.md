# senior-data-engineer

> 构建可扩展数据管道、ETL/ELT 系统和数据基础设施的高级数据工程技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | senior-data-engineer |
| **作者** | alirezarezvani |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-senior-data-engineer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-data-engineer |
| **安全评级** | 🟢 Low |

## 功能概述
- 批处理和实时流式管道设计
- Airflow/Prefect/Dagster 编排配置生成
- 数据质量验证框架
- ETL 性能优化分析
- 数据建模模式（星型/雪花/数据金库）
- DataOps 最佳实践

## 使用场景
- 从零设计数据管道架构
- 优化现有 ETL/ELT 流程性能
- 建立数据质量监控体系

## 依赖和前提条件
- Python 3
- 可选：PyYAML

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| scripts/pipeline_orchestrator.py | 管道编排配置生成器 |
| scripts/data_quality_validator.py | 数据质量验证工具 |
| scripts/etl_performance_optimizer.py | ETL 性能优化器 |
| references/ | 数据建模、管道架构、DataOps 参考文档 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Python 脚本，无 shell 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地操作 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用 Python 标准库 + PyYAML |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅生成配置文件和报告 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读，结构良好 |

**综合评级: 🟢 Low**
**风险摘要:** 专业的数据工程工具集，代码质量高，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
