# Chain of Density

> 渐进式摘要生成工具（Chain of Density 方法）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Chain of Density |
| **作者** | killerapp |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/killerapp-chain-of-density |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/killerapp/chain-of-density |
| **安全评级** | 🟢 Low |

## 功能概述
- 使用信息密度递增法生成摘要
- 多轮迭代优化摘要质量
- 保留关键信息同时提高信息密度
- 支持长文本的高质量摘要

## 使用场景
- 将长篇文章逐步压缩为高密度摘要
- 为学术论文生成不同详略程度的摘要

## 依赖和前提条件
- Python 运行环境
- GitHub API

## 包含文件
- `README.md`
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
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23