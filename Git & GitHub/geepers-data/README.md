# Geepers Data

> 通过单一端点获取 17 个权威数据源的结构化数据，包括 arXiv、美国人口普查局、GitHub、NASA、维基百科、PubMed 等。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Geepers Data |
| **作者** | lukeslp |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/lukeslp-geepers-data |

## 功能概述
- 统一访问 17 个权威数据源（arXiv、Census、GitHub、NASA、Wikipedia、PubMed 等）
- 通过 `https://api.dr.eamer.dev` 单一 API 端点进行数据查询
- 支持跨数据源搜索，可指定来源 ID 和查询条件
- 提供学术论文、人口统计、代码仓库、太空数据、新闻、天气、金融等多领域数据
- 支持 YouTube 视频元数据、Wolfram Alpha 计算知识和网页存档快照
- 返回结构化 JSON 数据，便于编程处理

## 使用场景
- 需要从多个权威来源获取可引用数据进行学术研究
- 构建数据管道，将外部权威数据源整合到现有系统中
- 用外部上下文数据丰富现有数据集进行分析和可视化

## 依赖和前提条件
- 环境变量 `DREAMER_API_KEY`：需要设置 API 密钥
- 网络访问：需连接 `https://api.dr.eamer.dev`

## 安全状态
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

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
