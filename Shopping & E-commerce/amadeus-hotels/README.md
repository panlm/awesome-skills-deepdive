# amadeus-hotels

> 通过 Amadeus API 搜索酒店价格和房态，支持按城市、坐标和设施筛选

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | amadeus-hotels |
| **作者** | kesslerio |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-amadeus-hotels |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/amadeus-hotels |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Hotel Search: Find hotels by city code or coordinates
- Pricing: Get room rates and availability
- Details: Full offer info, cancellation policies, ratings
- Price Tracking: Monitor hotels and alert on price drops
- hotels HTPAR001,HTPAR002 \
- checkin 2026-03-15 \

## 依赖和前提条件
- Create account at https://developers.amadeus.com/self-service
- Create a new app to get API credentials
- Set environment variables:

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23