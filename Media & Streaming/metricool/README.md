# Metricool

> Metricool 社交媒体分析和排期工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Metricool |
| **作者** | willscott-v2 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/willscott-v2-metricool |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/willscott-v2/metricool |
| **安全评级** | 🟡 Medium |

## 功能概述
- Must be publicly accessible URL (S3, GCS, etc.)
- Recommended formats: PNG, JPG
- Square images work best for Instagram/Threads
- Wide images (1.91:1) work best for X/LinkedIn

## 使用场景
- 分析多平台社交媒体数据
- 规划和排期社交媒体内容
- 生成社交媒体表现报告

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
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
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
