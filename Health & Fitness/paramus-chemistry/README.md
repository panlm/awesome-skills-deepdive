# Paramus Professional Chemistry OS

> 化学分子和反应分析工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Paramus Professional Chemistry OS |
| **作者** | gressling |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/gressling-paramus-chemistry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gressling/paramus-chemistry |
| **安全评级** | 🟡 Medium |

## 功能概述
- Molecular weight, LogP, TPSA, hydrogen bond donors/acceptors
- SMILES/InChI conversion or validation
- Any property calculation from a SMILES string
- Thermodynamic properties (CoolProp fluids)
- Polymer/BigSMILES analysis
- Electrochemistry calculations
- Data science operations (DOE, PCA, clustering)
- Local: Download Paramus from https://cloud1.paramus.ai and start the tray app (runs on localhost:8765)

## 使用场景
- 查询化学分子的性质和结构
- 模拟化学反应和计算
- 获取化学安全数据和处理建议

## 依赖和前提条件
- macOS
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
