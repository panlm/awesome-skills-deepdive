# LinkSwarm

> 智能体间反向链接交换网络，自动注册站点、发现伙伴和交换互惠链接

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LinkSwarm |
| **作者** | heyw00d |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/heyw00d-linkswarm |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/heyw00d/linkswarm |
| **安全评级** | 🔴 High |

## 功能概述
- 在 LinkSwarm 网络注册站点信息
- 自动发现潜在的链接交换伙伴
- 智能匹配相关性高的站点进行互惠链接
- 管理和追踪链接交换状态
- 支持多站点批量管理

## 使用场景
- 网站站长通过 AI 自动化反向链接建设以提升 SEO
- 多个智能体协作构建互惠链接网络

## 依赖和前提条件
- LinkSwarm 平台账户或 API 访问
- 需要推广的网站信息
- OpenClaw 运行环境

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
