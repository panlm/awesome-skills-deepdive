# SearXNG Search engine For OpenClaw by Upsurge.ae

> 基于 SearXNG 的智能体隐私搜索雷达，解决搜索 API 高成本和隐私泄露双重问题

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | SearXNG Search engine For OpenClaw by Upsurge.ae |
| **作者** | upsurge911-lgtm |
| **版本** | 1.4.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/upsurge911-lgtm-upsurge-searxng |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/upsurge911-lgtm/upsurge-searxng |
| **安全评级** | 🟢 Low |

## 功能概述
- 集成 SearXNG 元搜索引擎保护隐私
- 零 API 成本替代商业搜索服务
- 聚合多个搜索引擎结果提高覆盖率
- 支持自定义搜索引擎组合和权重
- 搜索请求不被追踪和记录
- 支持多语言和区域化搜索

## 使用场景
- 智能体需要频繁搜索但希望控制 API 成本
- 对搜索隐私有严格要求的企业或个人
- 自建搜索基础设施实现完全数据自主

## 依赖和前提条件
- SearXNG 实例（自部署或公共实例）
- 网络访问权限

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `search.py`

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
