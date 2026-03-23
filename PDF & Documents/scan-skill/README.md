# Scan Skill

> 文档扫描处理技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Scan Skill |
| **作者** | itsnishi |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/itsnishi-scan-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/itsnishi/scan-skill |
| **安全评级** | 🟢 Low |

## 功能概述
- 文档图像扫描和处理
- 文本提取和数字化
- 扫描质量优化
- 多格式输出支持

## 使用场景
- 将实体文档扫描转换为数字文件
- 优化扫描文档的图像质量

## 依赖和前提条件
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。Prompt 注入：存在可疑 Prompt 模式；混淆/反分析：使用编码/解码操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23