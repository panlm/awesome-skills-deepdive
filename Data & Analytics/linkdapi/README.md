# linkdapi

> 使用 LinkdAPI Python SDK 访问 LinkedIn 职业档案和公司数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | linkdapi |
| **作者** | foontinz |
| **ClawHub** | https://clawskills.sh/skills/foontinz-linkdapi |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/foontinz/linkdapi |
| **安全评级** | 🟡 Medium |

## 功能概述
- 获取 LinkedIn 用户职业档案概览
- 查询公司信息
- 搜索职位列表
- 搜索人物档案
- 使用 uv 脚本模式运行一次性 Python 脚本
- 自动依赖管理和清理

## 使用场景
- LinkedIn 职业档案数据获取
- 公司信息研究
- 职位搜索和人才分析

## 依赖和前提条件
- uv（Python 包管理器）
- LinkdAPI API Key（linkdapi.com 注册）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，SDK 使用指南 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 uv run 执行 Python 脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向 LinkdAPI 发送查询请求 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 LinkdAPI API Key |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 linkdapi PyPI 包和 linkdapi.com 服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 API 授权范围内 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 获取 LinkedIn 职业档案等个人数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 访问 LinkedIn 个人和公司数据的第三方 API 客户端

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
