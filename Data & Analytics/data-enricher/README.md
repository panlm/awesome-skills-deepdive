# data-enricher

> 用邮箱地址丰富销售线索数据，并格式化导入 Notion

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | data-enricher |
| **作者** | visualdeptcreative |
| **ClawHub** | https://clawskills.sh/skills/visualdeptcreative-data-enricher |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/visualdeptcreative/data-enricher |
| **安全评级** | 🟡 Medium |

## 功能概述
- 从网站联系页面提取邮箱
- 从 Instagram Bio 获取联系邮箱
- 通过 Hunter.io API 搜索域名邮箱（置信度 >70%）
- 根据常见模式猜测邮箱地址
- 邮箱优先级排序（创始人 > hello@ > info@ > support@）
- 域名去重和 Notion 同步

## 使用场景
- B2B 销售线索邮箱发现
- 潜在客户数据丰富化
- 自动化外展前的数据准备

## 依赖和前提条件
- `HUNTER_API_KEY` 环境变量
- Notion 集成（用于去重和同步）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含数据丰富化流程 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯指令型，无脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Hunter.io 发送域名查询，向 Notion 同步数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 Hunter.io API Key |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Hunter.io 第三方服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 保存数据到工作区 JSON 文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 API 授权范围内 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 主动搜索和采集邮箱地址 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 使用第三方 API 采集邮箱数据，涉及个人信息处理

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
