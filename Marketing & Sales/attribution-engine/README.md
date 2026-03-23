# Attribution Engine

> 营销归因分析引擎

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Attribution Engine |
| **作者** | otherpowers |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/otherpowers-attribution-engine |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/otherpowers/attribution-engine |
| **安全评级** | 🟡 Medium |

## 功能概述
- 多渠道归因分析
- 转化路径追踪
- 营销贡献度计算
- 归因模型对比报告

## 使用场景
- 分析各营销渠道对转化的贡献度
- 优化营销预算分配基于归因分析结果

## 依赖和前提条件
- Instagram API
- TikTok API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23