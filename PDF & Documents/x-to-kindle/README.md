# X To Kindle

> 将网页和文章内容转换为 Kindle 可读格式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | X To Kindle |
| **作者** | brianlu365ai |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/brianlu365ai-x-to-kindle |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianlu365ai/x-to-kindle |
| **安全评级** | 🟡 Medium |

## 功能概述
- 将网页文章转换为 Kindle 兼容格式
- 支持批量内容转换
- 保持文档排版和图片
- 自动发送到 Kindle 设备

## 使用场景
- 将收藏的长文章批量转换并推送到 Kindle 阅读
- 将博客系列文章打包为 Kindle 电子书

## 依赖和前提条件
- Python 运行环境
- X (Twitter) API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `send_to_kindle.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23