# Grazer

> 内容抓取和聚合浏览工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Grazer |
| **作者** | scottcjn |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/scottcjn-grazer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/scottcjn/grazer |
| **安全评级** | 🔴 High |

## 功能概述
- 网页内容抓取和提取
- 信息流聚合浏览
- 内容过滤和分类
- 数据结构化输出

## 使用场景
- 抓取和聚合多个网站的内容信息
- 定期采集目标网页的更新内容

## 依赖和前提条件
- API 密钥
- Python 运行环境
- Node.js
- Python pip
- npm
- AWS
- Discord API
- GitHub API

## 包含文件
- `BCOS.md`
- `DEPLOY.md`
- `INTEGRATION.md`
- `ORIGINAL_README.md`
- `PUBLISH_CHECKLIST.md`
- `README.md`
- `SECURITY.md`
- `SKILL.md`
- `STATUS.md`
- `_meta.json`
- `config.example.json`
- `debian`
- `grazer`
- `homebrew`
- `logo.txt`
- `package-lock.json`
- `package.json`
- `profile.example.json`
- `publish.sh`
- `requirements.txt`
- `setup.py`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23