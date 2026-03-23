# 4chan-reader

> 4chan 论坛内容读取和分析工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | 4chan-reader |
| **作者** | aiasisbot61 |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/aiasisbot61-4chan-reader |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aiasisbot61/4chan-reader |
| **安全评级** | 🟢 Low |

## 功能概述
- 4chan 帖子和线程抓取
- 内容过滤和分类
- 趋势话题发现
- 数据结构化输出

## 使用场景
- 监控 4chan 上特定话题的讨论动态
- 从 4chan 讨论中发现新兴趋势和话题

## 依赖和前提条件
- Python 运行环境

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
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。数据外泄：存在外部 API 调用




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23