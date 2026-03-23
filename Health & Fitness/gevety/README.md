# Gevety MCP

> Gevety 健康管理平台集成

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Gevety MCP |
| **作者** | moclippa |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/moclippa-gevety |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/moclippa/gevety |
| **安全评级** | 🟡 Medium |

## 功能概述
- Go to https://gevety.com/settings
- Click "Developer API" tab
- Click "Generate Token"
- Copy the token (starts with `gvt_`)
- Metabolic: Blood sugar, insulin, lipids
- Cardiovascular: Heart health markers
- Inflammatory: hs-CRP, homocysteine
- Hormonal: Thyroid, testosterone, cortisol

## 使用场景
- 集成 Gevety 健康管理平台功能
- 管理健康数据和健康档案
- 获取个性化健康建议

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
