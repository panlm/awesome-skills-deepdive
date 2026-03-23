# boj-mcp

> 访问日本银行（BOJ）统计数据 — 物价指数、资金流向、汇率等

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | boj-mcp |
| **作者** | ajtgjmdjp |
| **ClawHub** | https://clawskills.sh/skills/ajtgjmdjp-boj-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ajtgjmdjp/boj-mcp |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Look up Corporate Goods Price Index (CGPI/企業物価指数) trends
- Analyze Services Producer Price Index (SPPI/企業向けサービス価格指数)
- Retrieve Flow of Funds data (資金循環統計)
- Access Balance of Payments statistics (国際収支統計)
- Review BIS international statistics
- Explore TANKAN survey results (短観)

## 依赖和前提条件
- 

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
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