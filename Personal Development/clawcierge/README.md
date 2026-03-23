# clawcierge

> AI 礼宾服务 — 旅行、餐饮和生活方式推荐

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clawcierge |
| **作者** | tmansmann0 |
| **ClawHub** | https://clawskills.sh/skills/tmansmann0-clawcierge |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tmansmann0/clawcierge |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Install locally:
- Or just read them from the URLs above!
- Base URL: `https://fkuwhldhdgcxllnofixj.supabase.co/functions/v1`
- H "Content-Type: application/json" \
- d '{"name": "my-agent"}'
- Response (without email):

## 依赖和前提条件
- Or just read them from the URLs above!**
- Base URL:** `https://fkuwhldhdgcxllnofixj.supabase.co/functions/v1`
- 

## 包含文件
- `BACKUP.md`
- `EMAIL.md`
- `HEARTBEAT.md`
- `MESSAGING.md`
- `README.md` — 中文说明文档
- `SHARING.md`
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `package.json` — 配置/数据文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟡 Medium | 包含文件读写操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23