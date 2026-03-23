# Twitter/X Reader

> Twitter/X 内容读取和分析工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Twitter/X Reader |
| **作者** | iheardulkbtc |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/iheardulkbtc-twitter-reader |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iheardulkbtc/twitter-reader |
| **安全评级** | 🟡 Medium |

## 功能概述
- 读取 Twitter 推文和时间线
- 用户资料和推文搜索
- 内容分析和统计
- 数据导出功能

## 使用场景
- 监控特定话题的 Twitter 讨论动态
- 抓取和分析行业 KOL 的推文内容

## 依赖和前提条件
- API 密钥
- X (Twitter) API

## 包含文件
- `INSTALLATION.md`
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`
- `test_skill.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23