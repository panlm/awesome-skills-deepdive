# Garmin Health Analysis

> Garmin 健康数据综合分析工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Garmin Health Analysis |
| **作者** | eversonl |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/eversonl-garmin-health-analysis |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eversonl/garmin-health-analysis |
| **安全评级** | 🟡 Medium |

## 功能概述
- High (75-100): Fully recharged, ready for high intensity
- Medium (50-74): Moderate energy, good for regular activity
- Low (25-49): Limited energy, recovery needed
- Very Low (0-24): Depleted, prioritize rest
- Excellent (90-100): Optimal restorative sleep
- Good (80-89): Quality sleep with minor issues
- Fair (60-79): Adequate but could improve
- Poor (0-59): Significant sleep deficiencies

## 使用场景
- 综合分析 Garmin 的健康和运动数据
- 生成周/月度健康分析报告
- 识别训练和恢复的最佳模式

## 依赖和前提条件
- Node.js / npm
- Python / pip
- OAuth

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `config.example.json`
- `install.sh`
- `references`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
