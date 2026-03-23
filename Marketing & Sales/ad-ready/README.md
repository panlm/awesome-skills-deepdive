# Ad-Ready

> 广告素材快速生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ad-Ready |
| **作者** | pauldelavallaz |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/pauldelavallaz-ad-ready |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/ad-ready |
| **安全评级** | 🟡 Medium |

## 功能概述
- 快速生成广告创意素材
- 多平台广告格式适配
- 广告文案自动生成
- A/B 测试素材制作

## 使用场景
- 为多个广告平台快速生成适配尺寸的广告素材
- 批量制作广告创意的 A/B 测试版本

## 依赖和前提条件
- API 密钥
- Google API
- GitHub API
- Facebook API
- Instagram API
- TikTok API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `configs`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23