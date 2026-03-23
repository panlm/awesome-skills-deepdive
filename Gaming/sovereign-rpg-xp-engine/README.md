# sovereign-rpg-xp-engine

> RPG 生活经验值引擎，将现实任务转化为角色扮演游戏的 XP 和等级系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sovereign-rpg-xp-engine |
| **作者** | ryudi84 |
| **ClawHub** | https://clawskills.sh/skills/ryudi84-sovereign-rpg-xp-engine |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryudi84/sovereign-rpg-xp-engine |
| **安全评级** | 🟢 Low |

## 功能概述
- 将现实生活任务转化为 RPG 经验值系统
- 五大属性追踪：力量、智力、纪律、社交、创造力
- XP 计算含多种加成：连续签到、早起、组合、每日首任务
- 等级公式：100 × (当前等级^1.5)
- 成就系统和历史记录
- 角色状态保存在 data/character.json

## 使用场景
- 个人习惯养成的游戏化管理
- 将日常任务转化为角色升级体验
- 激励用户完成健身、学习等任务

## 依赖和前提条件
- 无外部依赖（纯文档/数据型技能）
- 需要本地 data/ 目录存储角色状态

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | XP 计算规则和角色系统设计文档 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯文档，无脚本执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络请求，所有数据存储在本地 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证相关内容 |
| SEC-04 供应链风险 | 🟢 Safe | 无依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅读写 data/character.json（角色数据），范围有限 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯规则文档 |
| SEC-07 越权操作 | 🟢 Safe | 无系统操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无 cron 或后台服务 |
| SEC-09 信息采集 | 🟢 Safe | 仅记录用户自愿提供的任务完成信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 规则清晰透明 |

**综合评级: 🟢 Low**
**风险摘要:** 纯本地的 RPG 规则引擎文档，无网络、无脚本，安全风险极低。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
