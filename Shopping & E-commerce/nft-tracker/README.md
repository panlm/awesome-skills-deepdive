# nft-tracker

> NFT 资产追踪和价格监控

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | nft-tracker |
| **作者** | ianalloway |
| **ClawHub** | https://clawskills.sh/skills/ianalloway-nft-tracker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ianalloway/nft-tracker |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- BAYC: `0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d`
- MAYC: `0x60e4d786628fea6478f785a6d7e704777c86a7c6`
- CryptoPunks: `0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb`
- H "X-API-KEY: $OPENSEA_API_KEY" | jq '.'
- Reservoir API is free and doesn't require authentication for basic queries
- Rate limits apply - cache responses when possible

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