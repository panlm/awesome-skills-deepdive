# data-lineage-tracker

> 追踪建筑行业数据的来源、转换和流向，用于审计和合规

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | data-lineage-tracker |
| **作者** | datadrivenconstruction |
| **ClawHub** | https://clawskills.sh/skills/datadrivenconstruction-data-lineage-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction/data-lineage-tracker |
| **安全评级** | 🟢 Low |

## 功能概述
- 追踪数据来源和转换步骤
- 记录数据流和实体关系
- 支持 10 种转换类型（ETL、聚合、过滤等）
- 数据完整性校验（checksum）
- 版本控制和变更追踪
- 审计日志和合规报告

## 使用场景
- 建筑项目数据审计追踪
- 合规性报告生成
- 数据问题溯源和调试

## 依赖和前提条件
- Python 3
- 文件系统权限

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含数据模型和实现代码 |
| instructions.md | 使用说明 |
| claw.json | 配置文件 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 Python 代码，无 shell 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地操作 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用 Python 标准库 |
| SEC-05 文件系统篡改 | 🟢 Safe | 在指定目录操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | instructions.md 为标准指令 |
| SEC-07 越权操作 | 🟢 Safe | claw.json 仅声明 filesystem 权限 |
| SEC-08 持久化机制 | 🟢 Safe | 数据存储为预期功能 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯本地数据追踪工具，仅使用标准库，安全性良好

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
