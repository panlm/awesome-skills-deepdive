# Linkfuse

> 链接管理和追踪工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Linkfuse |
| **作者** | oliverw |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/oliverw-linkfuse |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/oliverw/linkfuse |
| **安全评级** | 🟡 Medium |

## 功能概述
- 链接缩短和管理
- 点击追踪和分析
- 自定义短链域名
- 链接分组管理

## 使用场景
- 创建可追踪的营销短链接
- 分析链接点击数据优化营销渠道

## 依赖和前提条件
- API 密钥
- Bearer Token
- Node.js
- Chrome 浏览器

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
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23