# Book Reader - Learn & Grow Every Day

> 电子书阅读和内容提取工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Book Reader - Learn & Grow Every Day |
| **作者** | josharsh |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/josharsh-book-reader |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/josharsh/book-reader |
| **安全评级** | 🟡 Medium |

## 功能概述
- 读取和解析多种电子书格式
- 提取书籍章节和目录结构
- 文本内容搜索和检索
- 阅读进度管理

## 使用场景
- 提取技术书籍的关键章节用于学习笔记
- 批量处理电子书内容生成摘要

## 依赖和前提条件
- Python 运行环境
- Pandoc
- AWS
- Redis

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `book-reader.sh`
- `skill.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 5 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；供应链风险：需要安装外部依赖




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23