# umea-data

> 查询瑞典于默奥市开放数据：位置、设施、人口、环境等

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | umea-data |
| **作者** | simskii |
| **ClawHub** | https://clawskills.sh/skills/simskii-umea-data |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/simskii/umea-data |
| **安全评级** | 🟢 Low |

## 功能概述
- 查询于默奥市 13+ 种开放数据集
- 按坐标查找最近的设施（充电站、游泳场、游乐场等）
- 支持建筑许可、人口变化、犯罪统计等数据
- 距离计算和排序
- 无需 API Key，完全免费

## 使用场景
- 查找于默奥市附近设施
- 城市数据分析和研究
- 本地生活信息查询

## 依赖和前提条件
- curl, jq
- 无需 API Key

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| ORIGINAL_README.md | 原始说明 |
| scripts/query.sh | 数据集查询脚本 |
| scripts/nearby.sh | 最近位置搜索脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 curl 和 jq，参数处理安全 |
| SEC-02 数据外泄 | 🟢 Safe | 仅查询公开 API（opendata.umea.se） |
| SEC-03 凭证获取 | 🟢 Safe | 无需凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖于默奥市官方 API |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 只读公开数据 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 仅查询公开数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 安全的公共开放数据查询工具，无需认证，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
