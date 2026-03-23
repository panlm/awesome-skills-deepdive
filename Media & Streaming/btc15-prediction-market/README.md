# BTC15 Prediction Market

> BTC15 预测市场参与工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BTC15 Prediction Market |
| **作者** | kamal-sutra |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/kamal-sutra-btc15-prediction-market |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kamal-sutra/btc15-prediction-market |
| **安全评级** | 🟡 Medium |

## 功能概述
- 支持通过命令行进行操作控制
- 提供自动化工作流集成
- 支持多种媒体格式和平台

## 使用场景
- 参与加密货币预测市场
- 分析预测市场趋势和赔率
- 管理预测仓位和收益

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
