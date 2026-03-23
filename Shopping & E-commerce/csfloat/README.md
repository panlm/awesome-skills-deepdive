# csfloat

> CS2 皮肤交易市场 CSFloat 数据查询和分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | csfloat |
| **作者** | bluesyparty-src |
| **ClawHub** | https://clawskills.sh/skills/bluesyparty-src-csfloat |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bluesyparty-src/csfloat |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- H "Authorization: $LISTING_ID; Content-Type: application/json" \
- d '{"asset_id": 21078095468, "type": "buy_now", "price": 8900, "description": "Just for show", "private": false}'
- Asset ids are from Steam

## 依赖和前提条件
- Get your API key: [https://csfloat.com/profile](https://csfloat.com/profile), under the Developer tab
- Generate a key by pressing "New Key"
- Set environment variables:

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23