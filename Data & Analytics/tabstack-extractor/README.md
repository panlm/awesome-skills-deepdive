# tabstack-extractor

> 使用 Tabstack API 从网站提取结构化数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | tabstack-extractor |
| **作者** | noblepayne |
| **ClawHub** | https://clawskills.sh/skills/noblepayne-tabstack-extractor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/noblepayne/tabstack-extractor |
| **安全评级** | 🟡 Medium |

## 功能概述
- JSON Schema 驱动的结构化数据提取
- 网页 Markdown 内容提取
- 支持重试逻辑和缓存机制
- 批量 URL 提取
- 多语言实现（Python + Bash + Babashka）
- 预定义的职位/新闻 Schema 模板

## 使用场景
- 批量网页数据结构化采集
- 新闻和职位信息自动抓取
- 网页内容存档和分析

## 依赖和前提条件
- `TABSTACK_API_KEY` 环境变量
- Python 3 + requests 或 Babashka

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件 |
| scripts/tabstack_api.py | Python API 封装 |
| scripts/tabstack_curl.sh | Bash API 封装 |
| references/ | API 参考、Schema 示例 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | Python/Bash 脚本，无危险命令 |
| SEC-02 数据外泄 | 🟡 Medium | 向 Tabstack API 发送 URL 供提取 |
| SEC-03 凭证获取 | 🟢 Safe | 从环境变量读取 API Key |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 Tabstack (tabstack.ai) 第三方服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅输出提取结果 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 API 权限内 |
| SEC-08 持久化机制 | 🟢 Safe | 缓存为预期功能 |
| SEC-09 信息采集 | 🟡 Medium | 用于网页数据采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 依赖第三方 Tabstack API 服务，URL 数据发送到外部

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
