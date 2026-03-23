# osint-graph-analyzer

> 从 OSINT 数据构建知识图谱，发现隐藏模式和关系

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | osint-graph-analyzer |
| **作者** | orosha-ai |
| **ClawHub** | https://clawskills.sh/skills/orosha-ai-osint-graph-analyzer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/orosha-ai/osint-graph-analyzer |
| **安全评级** | 🟡 Medium |

## 功能概述
- CSV/JSON 数据导入 Neo4j 图数据库
- 社区检测算法（GDS）
- 中心性分析（PageRank、度中心性、介数中心性）
- 最短路径分析
- JSON 导出可视化（D3.js/Cytoscape）
- 完全本地运行，无外部 API 调用

## 使用场景
- 调查分析工作流
- 威胁情报分析
- 社交网络关系分析

## 依赖和前提条件
- Neo4j 数据库（Docker 推荐）
- Python 3 + neo4j 驱动

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| ORIGINAL_README.md | 原始说明 |
| scripts/osint-graph.py | 图分析核心脚本 |
| data/nodes.csv | 示例节点数据 |
| data/edges.csv | 示例边数据 |

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
| SEC-03 凭证获取 | 🟡 Medium | Neo4j 默认密码硬编码（neo4j/password），仅用于本地开发 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 neo4j Python 驱动 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅输出 JSON 导出文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 数据存储在 Neo4j 中，属预期功能 |
| SEC-09 信息采集 | 🟡 Medium | OSINT 工具本质上用于信息收集分析 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** OSINT 分析工具，Neo4j 默认密码硬编码，完全本地运行

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
