# OpenSETI

> Distributed SETI scanner - contribute compute power to analyze real radio telescope data from Breakthrough Listen. Earn tokens when your analysis discovers anomalies. Use when setting up distributed alien signal detection, running SETI scans, or contributing to the OpenSETI network.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenSETI |
| **作者** | synergysize |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/synergysize-openseti-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/synergysize/openseti-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- Narrowband signals (< 10 Hz bandwidth) - Natural sources are broadband
- Doppler drift - Frequency shift indicating non-terrestrial origin
- High SNR - Strong signals above noise floor
- Hydrogen line proximity - 1420.405 MHz is the "water hole"
- Non-RFI patterns - Doesn't match known Earth interference
- `openseti register <wallet>` - Register your Solana wallet

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23