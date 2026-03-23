# Rune - Self-Improving AI Memory

> Rune 符文工具 — 结构化知识编码和检索

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Rune - Self-Improving AI Memory |
| **作者** | thebobloblaw |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/thebobloblaw-rune |
| **安全评级** | 🔴 High |

## 功能概述
- 结构化知识编码和存储
- 符号化信息检索
- 知识片段关联和组合
- 自定义编码方案支持

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Node.js 及相关依赖
- OpenAI API 密钥
- Anthropic API 密钥
- Medium 账户
- 相关服务 API 密钥
- 运行 install.sh 安装脚本

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23