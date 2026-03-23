# senior-data-scientist

> 世界级数据科学技能：统计建模、实验设计、因果推断和预测分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | senior-data-scientist |
| **作者** | alirezarezvani |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-senior-data-scientist |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-data-scientist |
| **安全评级** | 🟢 Low |

## 功能概述
- A/B 测试设计和样本量计算
- 双比例 Z 检验和 Bonferroni 校正
- 特征工程管道（Scikit-learn、XGBoost）
- 模型评估（AUC-ROC、AUC-PR、SHAP）
- MLflow 实验追踪
- 差异中的差异（DiD）因果分析

## 使用场景
- 设计和分析 A/B 测试实验
- 构建和评估机器学习模型
- 观察数据的因果推断分析

## 依赖和前提条件
- Python 3（NumPy、Pandas、Scikit-learn）
- 可选：R、SQL

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，核心工作流代码 |
| scripts/experiment_designer.py | 实验设计器 |
| scripts/feature_engineering_pipeline.py | 特征工程管道 |
| scripts/model_evaluation_suite.py | 模型评估套件 |
| references/ | 实验设计框架、特征工程模式、高级统计方法 |

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
| SEC-04 供应链风险 | 🟢 Safe | 使用知名科学计算库 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅生成结果文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读，结构良好 |

**综合评级: 🟢 Low**
**风险摘要:** 专业的数据科学工具集，代码质量高，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
