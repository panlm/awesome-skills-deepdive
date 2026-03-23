# Scam Guards

> 反诈骗防护工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Scam Guards |
| **作者** | y01026350884-cyber |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/y01026350884-cyber-scam-guards |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/y01026350884-cyber/scam-guards |
| **安全评级** | 🟢 Low |

## 功能概述
- 识别常见诈骗模式
- 可疑内容自动检测
- 安全警告和建议
- 诈骗特征数据库

## 使用场景
- 自动检测消息中的诈骗特征并预警
- 评估链接和内容的安全可信度

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`
- `test_scenarios`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23