# Customer Service Scripts

> 生成上下文感知的客服回复脚本，帮助客服人员高效应对各类客户咨询

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Customer Service Scripts |
| **作者** | user520512 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/user520512-cs-scripts |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/user520512/cs-scripts |
| **安全评级** | 🟢 Low |

## 功能概述
- 根据客户问题上下文生成精准回复
- 支持多种客服场景模板
- 自动匹配知识库中的解决方案
- 语气和风格可自定义调节
- 多语言客服回复支持
- 回复质量评分与优化建议

## 使用场景
- 客服团队快速生成标准化且个性化的回复
- 新客服人员培训和辅助应答
- 处理大量重复性客户咨询

## 依赖和前提条件
- OpenClaw 环境已配置
- 客服知识库或FAQ文档（可选）

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
