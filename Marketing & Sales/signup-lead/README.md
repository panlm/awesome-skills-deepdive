# Signup Lead

> 注册线索获取工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Signup Lead |
| **作者** | waqas-orcalo |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/waqas-orcalo-signup-lead |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/waqas-orcalo/signup-lead |
| **安全评级** | 🟢 Low |

## 功能概述
- 注册数据采集
- 线索来源追踪
- 转化分析
- 线索评分

## 使用场景
- 追踪和分析各渠道的注册线索数据
- 优化注册流程提高线索质量

## 依赖和前提条件
- API 密钥

## 包含文件
- `README.md`
- `SKILL.md`
- `SKILL.yaml`
- `_meta.json`

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