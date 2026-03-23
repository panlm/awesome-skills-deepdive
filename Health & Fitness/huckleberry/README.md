# Huckleberry

> Huckleberry 婴儿睡眠追踪工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Huckleberry |
| **作者** | jayhickey |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/jayhickey-huckleberry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jayhickey/huckleberry |
| **安全评级** | 🟢 Low |

## 功能概述
- Python 3.11+
- huckleberry-api
- 1 oz ≈ 30 ml
- 1 lb ≈ 0.45 kg
- 1 inch ≈ 2.54 cm

## 使用场景
- 追踪婴儿的睡眠模式和规律
- 获取婴儿睡眠训练建议
- 分析婴儿的睡眠数据趋势

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
