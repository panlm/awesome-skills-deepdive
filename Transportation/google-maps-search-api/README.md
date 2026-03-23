# Google Maps Search Api

> This skill is designed to help users automatically extract business data from Google Maps search results. When a user asks to "find coffee shops in New York," "search for dental clinics," or "extract business leads from Google Maps," the agent should proactively apply this skill.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Google Maps Search Api |
| **作者** | phheng |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/phheng-google-maps-search-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/phheng/google-maps-search-api |
| **安全评级** | 🟢 Low |

## 功能概述
- 🚀 Stable & crash-free execution
- ⚡ Fast response times
- 🔧 No configuration headaches
- 📦 Plug & play installation
- 💬 Professional support
- Type: `string`

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
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
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；混淆/反分析：使用编码/解码操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23