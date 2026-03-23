# Detox Counter

> 排毒和戒断天数计数器

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Detox Counter |
| **作者** | jhillin8 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/jhillin8-detox-counter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jhillin8/detox-counter |
| **安全评级** | 🟢 Low |

## 功能概述
- Sugar Detox - Eliminate refined sugars and sweetened foods
- Juice Cleanse - Liquid-only nutrition, typically 3–7 days
- Whole30 - 30-day elimination of grains, legumes, dairy, sugar, and additives
- Elimination Diet - Remove suspected food triggers (dairy, gluten, nightshades, etc.)
- Custom - Define your own protocol and tracked symptom categories
- Set realistic expectations. Most detoxes involve an adjustment period (day 2–4) where symptoms spike before improving. This is normal
- Log consistently. Daily check-ins reveal patterns that sporadic logging misses. Even a 30-second note counts
- Use your milestone calendar. Knowing what's "normal" for day 5 of Whole30 helps you stay committed when cravings hit

## 使用场景
- 记录和追踪排毒/戒断天数
- 设定目标和查看里程碑
- 获取坚持的激励提示

## 依赖和前提条件
- 参见 SKILL.md 获取详细依赖信息

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
