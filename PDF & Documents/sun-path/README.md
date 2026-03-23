# Sun Path & Environmental Analysis

> Generates a sun path diagram, calculates solar position, performs building shadow analysis, and analyzes thermal comfort.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sun Path & Environmental Analysis |
| **作者** | qrost |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/qrost-sun-path |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/qrost/sun-path |
| **安全评级** | 🟡 Medium |

## 功能概述
- `pysolar` (solar calculations)
- `matplotlib` (plotting)
- `pytz` (timezone handling)
- `shapely` (geometry calculations for shadows)
- `numpy` (math)
- `rasterio` (for terrain/DEM shadow; optional for DEM features)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `PUBLISH.md`
- `SKILL.md`
- `_meta.json`
- `clawhub.json`
- `requirements.txt`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23