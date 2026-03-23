# Ad-Ready Pro

> 专业版广告素材创作工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ad-Ready Pro |
| **作者** | pauldelavallaz |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/pauldelavallaz-ad-ready-pro |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready-pro |
| **安全评级** | 🟡 Medium |

## 功能概述
- 专业级广告素材设计
- 高级广告文案生成
- 品牌一致性保障
- 多渠道素材输出

## 使用场景
- 为品牌广告活动创建专业级广告素材
- 生成跨渠道一致的品牌广告内容

## 依赖和前提条件
- API 密钥
- GitHub API
- Facebook API
- Instagram API
- TikTok API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23