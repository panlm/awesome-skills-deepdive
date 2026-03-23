# pine-voice

> Pine 语音助手 — 个性化语音交互体验

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | pine-voice |
| **作者** | bojieli |
| **ClawHub** | https://clawskills.sh/skills/bojieli-pine-voice |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bojieli/pine-voice |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Important: The voice agent can only speak English. Supported countries: US/CA/PR (+1), UK (+44), AU (+61), NZ (+64), SG (+65), IE (+353), HK (+852).
- Calling customer service to negotiate bills, request credits, or resolve issues
- Scheduling meetings or appointments by phone
- Making restaurant reservations
- Calling businesses to inquire about services or availability
- Following up with contacts on behalf of the user

## 依赖和前提条件
- Recommended:** Claude Sonnet/Opus 4.5+, GPT-5.2+, Gemini 3 Pro
- Not recommended:** Gemini 3 Flash, or models without thinking capabilities

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

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