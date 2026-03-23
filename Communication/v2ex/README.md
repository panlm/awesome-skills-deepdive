# v2ex

> V2EX API 2.0 完整集成，访问 V2EX 技术论坛的话题、节点、通知等全部数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | v2ex |
| **作者** | timqian |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/timqian-v2ex |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/timqian/v2ex |
| **安全评级** | 🔴 High |

## 功能概述
- 获取 V2EX 最新和热门话题列表
- 按节点浏览和搜索话题内容
- 查看和管理个人通知消息
- 获取话题详情和回复内容
- 浏览节点信息和分类结构
- 支持用户资料查询

## 使用场景
- 技术人员通过 AI 助手快速浏览 V2EX 热门讨论
- 监控特定节点的新话题获取行业动态
- 自动汇总 V2EX 上与特定技术相关的讨论

## 依赖和前提条件
- V2EX API Token（部分功能需要）
- V2EX 账户（访问个人数据时需要）

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
