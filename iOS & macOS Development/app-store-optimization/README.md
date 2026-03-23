# app-store-optimization

> 全面的 App Store 优化(ASO)工具包，涵盖关键词研究、元数据优化、竞品分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | app-store-optimization |
| **作者** | alirezarezvani |
| **ClawHub** | https://clawskills.sh/skills/alirezarezvani-app-store-optimization |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/app-store-optimization |
| **安全评级** | 🟢 Low |

## 功能概述
- 关键词研究与分析（搜索量、竞争度、长尾词）
- 平台特定元数据优化（Apple/Google 字符限制验证）
- 竞品分析与差距识别
- ASO 健康评分（0-100 分）
- A/B 测试规划（样本量计算、统计显著性）
- 多语言本地化策略
- 用户评论情感分析
- 发布前检查清单生成

## 使用场景
- 新应用上线前的完整 ASO 优化
- 竞品策略分析与关键词差距发现
- 多语言市场拓展的本地化规划

## 依赖和前提条件
- Python 3.7+
- 无外部包依赖（仅标准库）

## 包含文件
SKILL.md, 8 个 Python 模块（keyword_analyzer.py, metadata_optimizer.py 等）, references/（最佳实践指南）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 Python 计算逻辑，无系统命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 所有数据本地处理，无网络请求 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取任何凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅输出 JSON 格式结果 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理用户提供的数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码结构清晰，纯分析工具 |

**综合评级: 🟢 Low**
**风险摘要:** 纯知识型分析工具，无系统交互，安全性高

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
