# gamification-xp

> 通过 XP、等级、徽章和连续签到实现生产力游戏化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gamification-xp |
| **作者** | chipagosfinest |
| **ClawHub** | https://clawskills.sh/skills/chipagosfinest-gamification-xp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chipagosfinest/gamification-xp |
| **安全评级** | 🟡 Medium |

## 功能概述
- XP 经验值系统
- 等级公式 XP = 50 * (level²)
- 连续签到最高 2.0x 加成
- 徽章和成就系统
- 排行榜（多用户支持）
- 问责和赚回机制

## 使用场景
- 将日常任务转化为 XP 奖励
- 追踪习惯连续签到和等级
- 多用户生产力竞赛

## 依赖和前提条件
Supabase (SUPABASE_URL, SUPABASE_SERVICE_KEY)

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 API 接口文档，无可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 与 Supabase 云服务通信 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 SUPABASE_SERVICE_KEY（高权限密钥） |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Supabase 云服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无本地文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | API 有明确权限边界 |
| SEC-08 持久化机制 | 🟢 Safe | 无本地持久化 |
| SEC-09 信息采集 | 🟡 Medium | 存储用户游戏化数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 接口定义清晰 |

**综合评级: 🟡 Medium**
**风险摘要:** 使用 Supabase service_key 有较高数据库权限，需妥善保管

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
